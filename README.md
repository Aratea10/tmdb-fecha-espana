# 🎬 TMDB Estrenos España

<div align="center">

[![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![themoviedatabase](https://img.shields.io/badge/themoviedatabase-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white)](https://www.themoviedb.org/)

</div>

Script interactivo en Python que te permite consultar la **fecha de estreno comercial en España** de cualquier película, usando la API de [The Movie Database (TMDB)](https://www.themoviedb.org/).

Solo tienes que escribir el título de la película en español y el script te devuelve la fecha de estreno en cines en formato `dd/mm/aaaa`.

## ✨ Características
- 🔍 **Búsqueda en español**: Escribe el título de la película como lo conoces en España.
- 🎯 **Solo estrenos comerciales**: Filtra únicamente el estreno en cines (theatrical), ignorando premieres y preestrenos.
- 📅 **Formato español**: Fecha en formato `dd/mm/aaaa`.
- 💬 **Interfaz tipo chat**: Ejecutas el script una vez y puedes consultar todas las películas que quieras.

## 🚀 Instalación y Puesta en Marcha
### 1. Clona el repositorio
```git
git clone https://github.com/Aratea10/tmdb-fecha-espana.git
cd tmdb-fecha-espana
```


### 2. Crea y activa el entorno virtual
Crear entorno:
```bash
python -m venv .venv
```

Activar (Windows PowerShell)
```bash
source .venv/bin/activate
```

### 3. Instala las dependencias
```bash
pip install -r requirements.txt
```

### 4. Configura tu API Key de TMDB
1. Crea una cuenta en [themoviedb.org](https://www.themoviedb.org/signup)
2. Ve a **Configuración → API** y solicita una clave (es gratis para uso personal)
3. Crea un archivo `.env` en la raíz del proyecto:
   ```bash
   TMDB_API_KEY=tu_api_key_aqui
   ```

### 5. Ejecuta el script
```bash
python tmdb_estrenos_espana.py
```

## 💻 Uso
```python
🎬 BUSCADOR DE ESTRENOS COMERCIALES EN ESPAÑA
🔍 Película: el caballero oscuro
🎬 El caballero oscuro
📅 13/08/2008
🔍 Película: parásitos
🎬 Parásitos
📅 25/10/2019
🔍 Película: salir
👋 ¡Hasta luego!
```

```text
Escribe `salir`, `exit` o `q` para cerrar el programa.
```

## 📦 Crear ejecutable (opcional)
Si quieres generar un `.exe` para no depender de Python:
```bash
pip install pyinstaller
pyinstaller --onefile --console tmdb_estrenos_espana.py
```

El ejecutable se generará en `dist/tmdb_estrenos_espana.exe`. Recuerda copiar el archivo `.env` junto al `.exe` para que funcione.

## 🛠️ Tecnologías
- **Python 3.12**
- **Requests** — Peticiones HTTP a la API
- **python-dotenv** — Gestión de variables de entorno
- **PyInstaller** — Generación de ejecutables (opcional)

---

## 📄 Licencia
Este proyecto se distribuye bajo **Licencia MIT**.

---

## 👩‍💻 Autora
**Sara Gallego Méndez (Aratea10)**
