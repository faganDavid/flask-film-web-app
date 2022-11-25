import requests
from config import TMDB_API_KEY, TMDB_ENDPOINT, TMDB_DATA_ENDPOINT


def search_movie_data(movie_name):
    response = requests.get(TMDB_ENDPOINT, params={'api_key': TMDB_API_KEY, 'query': movie_name})
    movie_data = response.json()['results']

    return movie_data


def get_movie_data(movie_id):
    response = requests.get(f"{TMDB_DATA_ENDPOINT}/{movie_id} ", params={'api_key': TMDB_API_KEY, 'language': 'en-US'})
    movie_data = response.json()

    return movie_data

