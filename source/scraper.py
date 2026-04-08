import os
import requests
import csv
from bs4 import BeautifulSoup

# URL
URL = "https://www.boxofficemojo.com/chart/ww_top_lifetime_gross/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def query_movies(url, headers, dataset):
    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")

    if table is None:
        print("Error: no se encontró la tabla")
        return

    rows = table.find_all("tr")

    for i, row in enumerate(rows):
        cells = row.find_all("td")

        # Saltar cabecera o filas incompletas
        if i == 0 or len(cells) < 5:
            continue

        try:
            rank = cells[0].get_text(strip=True)

            # título + link
            title_tag = cells[1].find("a")
            title = title_tag.get_text(strip=True) if title_tag else cells[1].get_text(strip=True)

            movie_url = ""
            if title_tag and title_tag.get("href"):
                movie_url = "https://www.boxofficemojo.com" + title_tag["href"]

            # columnas correctas
            worldwide = cells[2].get_text(strip=True)
            domestic = cells[3].get_text(strip=True)
            foreign = cells[4].get_text(strip=True)

            element = [
                rank,
                title,
                worldwide,
                domestic,
                foreign,
                movie_url
            ]

            dataset.append(element)

        except Exception as e:
            print("Error procesando fila:", e)


def main():
    print("Generando dataset de películas...")

    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "..", "dataset", "movies_dataset.csv")

    dataset = []

    # HEADER FINAL (coherente)
    header = [
        "rank",
        "title",
        "worldwide_box_office",
        "domestic_box_office",
        "foreign_box_office",
        "movie_url"
    ]

    dataset.append(header)

    query_movies(URL, HEADERS, dataset)

    # Crear carpeta si no existe
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Guardar CSV
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(dataset)

    print(f"Dataset generado correctamente en: {file_path}")
    print(f"Número de películas: {len(dataset)-1}")


if __name__ == "__main__":
    main()