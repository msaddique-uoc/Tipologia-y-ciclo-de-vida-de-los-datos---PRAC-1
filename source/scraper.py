import requests
import csv
import os
import time

API_KEY = "thewdb"   # tu clave actual
BASE_URL = "https://www.omdbapi.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def search_movies(search_term: str):
    """
    Busca películas por término usando el parámetro s.
    """
    params = {
        "apikey": API_KEY,
        "s": search_term,
        "type": "movie"
    }

    response = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=20)
    response.raise_for_status()
    data = response.json()

    if data.get("Response") == "True":
        return data.get("Search", [])
    return []


def get_movie_details(imdb_id: str):
    """
    Obtiene detalle de una película usando el parámetro i.
    Aquí sí vienen campos como imdbRating y BoxOffice.
    """
    params = {
        "apikey": API_KEY,
        "i": imdb_id
    }

    response = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=20)
    response.raise_for_status()
    data = response.json()

    if data.get("Response") == "True":
        return data
    return {}


def get_movies():
    dataset = []
    seen_ids = set()

    search_terms = ["batman", "avengers", "spiderman", "superman"]

    for term in search_terms:
        print(f"Buscando: {term}")
        results = search_movies(term)

        for item in results:
            imdb_id = item.get("imdbID", "N/A")

            if imdb_id in seen_ids:
                continue

            details = get_movie_details(imdb_id)
            seen_ids.add(imdb_id)

            dataset.append({
                "title": details.get("Title", item.get("Title", "N/A")),
                "year": details.get("Year", item.get("Year", "N/A")),
                "imdb_rating": details.get("imdbRating", "N/A"),
                "box_office": details.get("BoxOffice", "N/A"),
                "type": details.get("Type", item.get("Type", "N/A")),
                "imdb_id": imdb_id,
                "imdb_url": f"https://www.imdb.com/title/{imdb_id}/"
            })

            time.sleep(0.5)

    return dataset


def main():
    dataset = get_movies()

    os.makedirs("dataset", exist_ok=True)

    output_file = os.path.join("dataset", "movies_dataset.csv")

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "title",
                "year",
                "imdb_rating",
                "box_office",
                "type",
                "imdb_id",
                "imdb_url"
            ]
        )
        writer.writeheader()
        writer.writerows(dataset)

    print(f"Dataset generado con {len(dataset)} películas")
    print(f"Archivo guardado en: {output_file}")


if __name__ == "__main__":
    main()