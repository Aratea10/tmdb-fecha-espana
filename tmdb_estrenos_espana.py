import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def buscar_titulo(query: str) -> list[dict] | None:
    """Busca películas y series por título y devuelve una lista de resultados."""
    response = requests.get(
        f"{BASE_URL}/search/multi",
        params={"api_key": API_KEY, "query": query, "language": "es-ES"},
    )
    if response.status_code != 200:
        print(f"Error de API: {response.status_code}")
        return None

    data = response.json()
    results = data.get("results", [])

    filtered_results = [r for r in results if r.get("media_type") in ["movie", "tv"]]
    return filtered_results


def obtener_fecha_comercial_espana(movie_id: int) -> str | None:
    """Obtiene la fecha de estreno comercial (theatrical) en España para películas"""
    response = requests.get(
        f"{BASE_URL}/movie/{movie_id}/release_dates", params={"api_key": API_KEY}
    )

    if response.status_code != 200:
        return None

    data = response.json()
    for pais in data.get("results", []):
        if pais["iso_3166_1"] == "ES":
            for fecha in pais.get("release_dates", []):
                if fecha.get("type") == 3:  # 3 = Theatrical
                    fecha_raw = fecha["release_date"]
                    dt = datetime.fromisoformat(fecha_raw.replace("Z", "+00:00"))
                    return dt.strftime("%d/%m/%Y")
    return None


def mostrar_opciones(resultados: list[dict]) -> dict | None:
    print(f"\n🔎 He encontrado {len(resultados)} coincidencias:")

    for i, item in enumerate(resultados, 1):
        tipo = "🎬 Película" if item["media_type"] == "movie" else "📺 Serie"
        titulo = (
            item.get("title") if item["media_type"] == "movie" else item.get("name")
        )

        fecha_raw = (
            item.get("release_date")
            if item["media_type"] == "movie"
            else item.get("first_air_date")
        )
        anio = fecha_raw[:4] if fecha_raw else "Fecha desconocida"

        print(f"   {i}. {titulo} ({anio}) - {tipo}")

    while True:
        try:
            seleccion = input("\n👉 Elige un número (o 0 para cancelar): ")
            if not seleccion:
                continue
            idx = int(seleccion)
            if idx == 0:
                return None
            if 1 <= idx <= len(resultados):
                return resultados[idx - 1]
            print("❌ Número inválido.")
        except ValueError:
            print("❌ Por favor, introduce un número.")


def main():
    print("🎬 BUSCADOR DE ESTRENOS (CINE Y SERIES)")
    print("=" * 45)
    while True:
        query = input("\n 🔍 Título: ").strip()
        if query.lower() in ["salir", "exit", "q"]:
            print("👋 ¡Hasta luego!")
            break
        if not query:
            continue

        resultados = buscar_titulo(query)

        if not resultados:
            print("❌ No encontré nada con ese nombre.")
            continue

        seleccion = None
        if len(resultados) == 1:
            seleccion = resultados[0]
        else:
            seleccion = mostrar_opciones(resultados)

        if not seleccion:
            continue

        tipo = seleccion["media_type"]
        nombre = seleccion.get("title") if tipo == "movie" else seleccion.get("name")
        item_id = seleccion["id"]

        print(f"\n✨ Has seleccionado: {nombre}")

        if tipo == "movie":
            fecha = obtener_fecha_comercial_espana(item_id)
            if fecha:
                print(f"📅 Estreno en cines (España): {fecha}")
            else:
                print(
                    "⚠️ No hay estreno comercial en España registrado (o ya pasó/no disponible)."
                )
        else:
            fecha_raw = seleccion.get("first_air_date")
            if fecha_raw:
                dt = datetime.strptime(fecha_raw, "%Y-%m-%d")
                print(f"📅 Primera emisión: {dt.strftime('%d/%m/%Y')}")
            else:
                print("⚠️ Fecha de emisión desconocida.")


if __name__ == "__main__":
    main()
