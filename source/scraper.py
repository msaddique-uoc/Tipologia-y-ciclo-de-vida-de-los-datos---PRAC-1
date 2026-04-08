import requests
import csv
import os

API_KEY = "thewdb"  # API gratuita
BASE_URL = "http://www.omdbapi.com/"

def get_movies():
    movies = []

    search_terms = ["batman", "avengers", "spiderman"]

    for term in search_terms:
        params = {
            "apikey": API_KEY,
            "s": term
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if "Search" in data:
            for item in data["Search"]:
                movies.append({
                    "title": item.get("Title", "N/A"),
                    "year": item.get("Year", "N/A"),
                    "imdb_id": item.get("imdbID", "N/A"),
                    "type": item.get("Type", "N/A")
                })

    return movies


def main():
    dataset = get_movies()

    os.makedirs("dataset", exist_ok=True)

    with open("dataset/movies_dataset.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "year", "imdb_id", "type"])
        writer.writeheader()
        writer.writerows(dataset)

    print(f"Dataset generado con {len(dataset)} películas")


if __name__ == "__main__":
    main()