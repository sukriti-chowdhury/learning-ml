"""
Write a Python program using Pandas to create a DataFrame from the given data and calculate the average rating of movies directed by Christopher Nolan.
data = {

    'Title': ['Inception', 'Dunkirk', 'Interstellar', 'The Prestige', 'Memento'],

    'Director': ['Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan'],

    'Rating': [8.8, 7.9, 8.6, 8.5, 8.4]

}
"""

import pandas as pd

data: dict = {
    'Title': ['Inception', 'Dunkirk', 'Interstellar', 'The Prestige', 'Memento'],
    'Director': ['Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan'],
    'Rating': [8.8, 7.9, 8.6, 8.5, 8.4]
}

moviesDF: pd.DataFrame = pd.DataFrame(data)
nolanMoviesDF: pd.DataFrame = moviesDF[moviesDF['Director'] == 'Christopher Nolan']
print(f"Average rating of Christopher Nolan's movies: {nolanMoviesDF['Rating'].mean():.2f}")