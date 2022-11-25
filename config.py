import uuid

SECRET_KEY = uuid.uuid4().hex

DATABASE_URI = "sqlite:///movies-collection.db"

# API KEY
TMDB_API_KEY = "b6a40714b26a94ce959cd4bf11de1be7"

# tmdb search movies endpoint
TMDB_ENDPOINT = "https://api.themoviedb.org/3/search/movie"

# tmdb get movie data endpoint
TMDB_DATA_ENDPOINT = "https://api.themoviedb.org/3/movie/"

# tmdb image url
TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500'