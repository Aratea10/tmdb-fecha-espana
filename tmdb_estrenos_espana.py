import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def buscar_pelicula(titulo: str) -> tuple[int, str] | None:
    """Busca una película por título en español y devuelve (id, nombre)."""
    response = requests.get(
        f"{BASE_URL}/search/movie",
        params={
            "api_key": API_KEY, 
            "query": titulo, 
            "language": "es-ES"
        },
    )
    if response.status_code != 200:
        print(f"Error de API: {response.status_code}")
        return None
    
    data = response.json()
    if data.get("results"):
        pelicula = data["results"][0]
        return pelicula["id"], pelicula["title"]
    return None


def obtener_fecha_comercial_espana(movie_id: int) -> str | None:
    """Obtiene la fecha de estreno comercial (theatrical) en España"""
    response = requests.get(
        f"{BASE_URL}/movie/{movie_id}/release_dates",
        params={"api_key": API_KEY}
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

def main():
    print("🎬 BUSCADOR DE ESTRENOS COMERCIALES EN ESPAÑA")
    print("=" * 45)
    while True:
        titulo = input("\n 🔍 Película: ").strip()
        if titulo.lower() in ["salir", "exit", "q"]:
            print("👋 ¡Hasta luego!")
            break
        if not titulo:
            continue
                    
        resultado=buscar_pelicula(titulo)
                    
        if not resultado:
            print("❌ No encontré esa película")
            continue
                    
        movie_id, nombre = resultado
        fecha = obtener_fecha_comercial_espana(movie_id)
                    
        if fecha:
            print(f"🎬 {nombre}")
            print(f"📅 {fecha}")
        else:
            print(f"🎬 {nombre}")
            print("⚠️ No hay estreno comercial en España registrado")
                    
if __name__ == "__main__":
    main()
