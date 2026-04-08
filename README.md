# Tipologia-y-ciclo-de-vida-de-los-datos---PRAC-1

# Dataset de películas mediante Web Scraping

## Autor
Muhammad Awais

---

## Descripción del proyecto
Este proyecto tiene como objetivo la extracción de datos de películas desde una página web pública mediante técnicas de web scraping en Python.

El proceso consiste en acceder a una página web, analizar su estructura HTML y extraer información relevante directamente desde una tabla de datos. A partir de esta información, se construye un dataset estructurado en formato CSV.

Durante el desarrollo del proyecto se identificaron limitaciones en algunas páginas web, como contenido dinámico o bloqueos anti-scraping. Por ello, se seleccionó una fuente alternativa con estructura HTML estable, garantizando así una extracción fiable, reproducible y coherente.

---

## Fuente de datos
Los datos se han extraído desde una página web pública accesible mediante HTTP, concretamente una tabla de recaudación de películas a nivel mundial.

---

## Estructura del repositorio

source/scraper.py → script principal de scraping  
dataset/movies_dataset.csv → dataset generado  
pdf/practica1_muhammad_awais.pdf → memoria del proyecto  
requirements.txt → dependencias necesarias  
README.md → documentación  

---

## Tecnologías utilizadas

Las principales librerías utilizadas son:

- `requests` → para realizar peticiones HTTP  
- `beautifulsoup4` → para analizar el HTML  

## Para instalarlas:
pip install -r requirements.txt


---

## Ejecución del código

Desde la raíz del proyecto:


python source/scraper.py


---

## El script realiza:

- Acceso a la página web  
- Identificación de la tabla HTML  
- Extracción de datos de películas  
- Procesamiento y limpieza de la información  
- Generación del dataset en formato CSV  

---

## El archivo generado se guarda en:


dataset/movies_dataset.csv


---

## Variables del dataset

El dataset incluye las siguientes variables:

- **rank** → posición en el ranking  
- **title** → título de la película  
- **worldwide_box_office** → recaudación global  
- **domestic_box_office** → recaudación en mercado doméstico  
- **foreign_box_office** → recaudación internacional  
- **movie_url** → enlace a la película  

---

## Consideraciones éticas

- Se han utilizado únicamente datos públicos  
- No se ha accedido a información privada o protegida  
- Se ha respetado el uso responsable del scraping  
- Se ha seleccionado una fuente estable para evitar sobrecarga del servidor  

---

## Dataset en Zenodo

El dataset ha sido publicado en Zenodo y puede accederse mediante el siguiente DOI:

👉 https://doi.org/10.5281/zenodo.19461976  

---

## Documentación

La memoria completa del proyecto se encuentra en la carpeta:


pdf/


---

## Repositorio

Proyecto disponible en:

👉 https://github.com/msaddique-uoc/Tipologia-y-ciclo-de-vida-de-los-datos---PRAC-1  

---

## Conclusión

Este proyecto demuestra cómo transformar datos no estructurados disponibles en la web en un dataset estructurado listo para su análisis.

Se han aplicado técnicas de web scraping mediante el uso de BeautifulSoup, permitiendo la extracción directa de datos desde HTML y garantizando la coherencia y calidad del dataset final.
