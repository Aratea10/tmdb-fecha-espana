import os
import re
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"


def buscar_pelicula(titulo: str, año: int | None = None) -> list[dict]:
    """Busca películas por título en español y opcionalmente por año."""
    params = {
        "api_key": API_KEY,
        "query": titulo,
        "language": "es-ES",
        "primary_release_year": año if año else None,
    }

    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(
        f"{BASE_URL}/search/movie",
        params=params,
    )
    if response.status_code != 200 or not response.json().get("results"):
        return []

    resultados = response.json()["results"]

    lista_peliculas = []
    for resultado in resultados:
        release_date = resultado.get("release_date", "")
        pelicula_año = int(release_date.split("-")[0]) if release_date else None

        lista_peliculas.append(
            {
                "tipo": "Película",
                "emoji": "🍿",
                "id": resultado["id"],
                "nombre": resultado["title"],
                "año": pelicula_año,
                "popularidad": resultado.get("popularity", 0),
            }
        )
    return lista_peliculas


def buscar_series(titulo: str, año: int | None = None) -> list[dict]:
    """Busca series por título en español y opcionalmente por año."""
    params = {
        "api_key": API_KEY,
        "query": titulo,
        "language": "es-ES",
        "first_air_date_year": año if año else None,
    }
    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(f"{BASE_URL}/search/tv", params=params)
    if response.status_code != 200 or not response.json().get("results"):
        return []
    resultados = response.json()["results"]
    lista_series = []
    for resultado in resultados:
        air_date = resultado.get("first_air_date", "")
        serie_año = int(air_date.split("-")[0]) if air_date else None

        lista_series.append(
            {
                "tipo": "Serie",
                "emoji": "📺",
                "id": resultado["id"],
                "nombre": resultado["name"],
                "año": serie_año,
                "popularidad": resultado.get("popularity", 0),
            }
        )
    return lista_series


def obtener_fecha_pelicula_espana(movie_id: int) -> str | None:
    """Obtiene la fecha de estreno (cines) de una película en España."""
    response = requests.get(
        f"{BASE_URL}/movie/{movie_id}/release_dates", params={"api_key": API_KEY}
    )
    if response.status_code != 200:
        return None
    data = response.json()
    for pais in data.get("results", []):
        if pais["iso_3166_1"] == "ES":
            for fecha in pais.get("release_dates", []):
                if fecha.get("type") == 3:
                    fecha_raw = fecha["release_date"]
                    dt = datetime.fromisoformat(fecha_raw.replace("Z", "+00:00"))
                    return dt.strftime("%d/%m/%Y")
    return None


def obtener_fecha_serie(tv_id: int) -> str | None:
    """Obtiene la fecha de estreno de la primera temporada de una serie."""
    response = requests.get(
        f"{BASE_URL}/tv/{tv_id}", params={"api_key": API_KEY, "language": "es-ES"}
    )
    if response.status_code != 200:
        return None
    fecha_raw = response.json().get("first_air_date")
    if fecha_raw:
        dt = datetime.strptime(fecha_raw, "%Y-%m-%d")
        return dt.strftime("%d/%m/%Y")
    return None


def extraer_año(titulo: str) -> tuple[str, int | None]:
    """Extrae el año del título si está presente. Ej: 'Dune 2021' -> ('Dune', 2021)"""
    match = re.search(r"\s(19\d{2}|20\d{2})$", titulo)
    if match:
        año = int(match.group(1))
        titulo_limpio = titulo[: match.start()].strip()
        return titulo_limpio, año
    return titulo, None


def main():
    print("🎬 BUSCADOR DE ESTRENOS EN ESPAÑA")
    print("=" * 50)
    print("Escribe el título (puedes añadir el año: 'Dune 2021')")
    print("Escribe 'salir' para cerrar")
    print("=" * 50)

    while True:
        entrada = input("\n🔍 Título: ").strip()

        if entrada.lower() in ["salir", "exit", "q"]:
            print("👋 Hasta luego")
            break

        if not entrada:
            continue

        titulo, año = extraer_año(entrada)

        peliculas = buscar_pelicula(titulo, año)
        series = buscar_series(titulo, año)

        todos = peliculas + series
        todos.sort(key=lambda x: x["popularidad"], reverse=True)

        if not todos:
            print("❌ No encontré ningún resultado")
            continue

        if len(todos) == 1:
            seleccion = todos[0]
        else:
            print("\n📋 Resultados encontrados:")
            print("-" * 50)
            for i, r in enumerate(todos[:8], 1):
                if r["tipo"] == "Película":
                    fecha = obtener_fecha_pelicula_espana(r["id"]) or "Sin fecha ES"
                else:
                    fecha = obtener_fecha_serie(r["id"]) or "Sin fecha"
                print(
                    f"  {i}. {r['emoji']} {r['nombre']} ({r['año']}) - {r['tipo']} - {fecha}"
                )
            print("-" * 50)

            try:
                opcion = input("👉 Elige un número (o Enter para el primero): ").strip()
                if opcion == "":
                    seleccion = todos[0]
                else:
                    seleccion = todos[int(opcion) - 1]
            except (ValueError, IndexError):
                print("⚠️ Opción no válida")
                continue

        if seleccion["tipo"] == "Película":
            fecha = obtener_fecha_pelicula_espana(seleccion["id"])
        else:
            fecha = obtener_fecha_serie(seleccion["id"])

        print(
            f"\n{seleccion['emoji']} {seleccion['nombre']} ({seleccion['año']}) - {seleccion['tipo']}"
        )
        if fecha:
            print(f"📅 Estreno en España: {fecha}")
        else:
            print("⚠️ No hay fecha de estreno en España registrada")

    if __name__ == "__main__":
        main()
