import requests
from bs4 import BeautifulSoup
import csv
import time
import os

BASE_URL = "https://www.themoviedb.org/movie?page="

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

def get_movies(page):
    url = BASE_URL + str(page)
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    movies = []

    cards = soup.select("div.card")

    for card in cards:
        try:
            title = card.select_one("h2")
            title = title.text.strip() if title else "N/A"

            rating = card.select_one("div.user_score_chart")
            rating = rating["data-percent"] if rating and rating.has_attr("data-percent") else "N/A"

            date = card.select_one("p")
            date = date.text.strip() if date else "N/A"

            link = card.select_one("a")
            link = "https://www.themoviedb.org" + link["href"] if link else "N/A"

            movies.append({
                "title": title,
                "rating": rating,
                "release_date": date,
                "movie_url": link
            })

        except:
            continue

    print(f"Películas encontradas en página {page}: {len(movies)}")
    return movies


def main():
    dataset = []

    for page in range(1, 6):
        print(f"Scrapeando página {page}...")
        movies = get_movies(page)
        dataset.extend(movies)
        time.sleep(2)

    if len(dataset) == 0:
        print("ERROR: No se extrajo ningún dato")
        return

    output_path = os.path.join("dataset", "movies_dataset.csv")

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=dataset[0].keys())
        writer.writeheader()
        writer.writerows(dataset)

    print(f"Dataset generado correctamente con {len(dataset)} registros")


if __name__ == "__main__":
    main()