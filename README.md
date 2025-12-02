# 🎬 TMDB Estrenos España

<div align="center">

[![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![themoviedatabase](https://img.shields.io/badge/themoviedatabase-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white)](https://www.themoviedb.org/)

</div>

Script interactivo en Python que te permite consultar la **fecha de estreno comercial en España** de películas y la **fecha de primera emisión** de series, usando la API de [The Movie Database (TMDB)](https://www.themoviedb.org/).

Solo tienes que escribir el título y el script te devolverá la información. Si hay varios resultados con el mismo nombre, te mostrará una lista para que elijas.

## ✨ Características
- 🎬 **Películas y Series**: Busca tanto películas como series de TV.
- 🔍 **Búsqueda inteligente**: Si hay coincidencias múltiples (mismo nombre, remakes, etc.), te permite elegir la correcta.
- 📅 **Fechas precisas**: 
  - **Películas**: Estreno en cines de España (theatrical).
  - **Series**: Fecha de primera emisión mundial.
- 🇪🇸 **Formato español**: Fechas siempre en formato `dd/mm/aaaa`.
- 💬 **Interfaz tipo chat**: Ejecutas el script una vez y puedes realizar múltiples consultas.

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
```text
🎬 BUSCADOR DE ESTRENOS (CINE Y SERIES)
=============================================

 🔍 Título: avatar

🔎 He encontrado 2 coincidencias:
   1. Avatar (2009) - 🎬 Película
   2. Avatar: La leyenda de Aang (2005) - 📺 Serie

👉 Elige un número (o 0 para cancelar): 1

✨ Has seleccionado: Avatar
📅 Estreno en cines (España): 18/12/2009

 🔍 Título: breaking bad

✨ Has seleccionado: Breaking Bad
📅 Primera emisión: 20/01/2008

 🔍 Título: salir
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
