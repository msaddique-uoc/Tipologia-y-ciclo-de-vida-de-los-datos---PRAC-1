import os
import requests
import csv
from bs4 import BeautifulSoup

# URL con tabla de películas
URL = "https://www.boxofficemojo.com/chart/ww_top_lifetime_gross/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def queryMovies(url, headers, dataset):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")

    currentIndex = 0

    for row in table.find_all("tr"):
        cells = row.find_all("td")

        if currentIndex > 0:  # saltar cabecera

            if len(cells) >= 4:
                rank = cells[0].text.strip()
                title = cells[1].text.strip()
                year = cells[2].text.strip()
                box_office = cells[3].text.strip()

                element = [rank, title, year, box_office]

                dataset.append(element)

        currentIndex += 1


# Directorio actual
currentDir = os.path.dirname(__file__)
filename = "movies_dataset.csv"
filePath = os.path.join(currentDir, "..", "dataset", filename)

# Crear dataset
dataset = []
header = ["Rank", "Title", "Year", "Box Office"]
dataset.append(header)

print("Generando dataset de películas...")

queryMovies(URL, HEADERS, dataset)

# Crear carpeta
os.makedirs(os.path.dirname(filePath), exist_ok=True)

# Guardar CSV
with open(filePath, 'w', newline='', encoding="utf-8") as csvFile:
    writer = csv.writer(csvFile)

    for row in dataset:
        writer.writerow(row)

print(f"Dataset generado correctamente en: {filePath}")