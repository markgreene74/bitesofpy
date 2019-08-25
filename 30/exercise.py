import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = "http://projects.bobbelderbos.com/pcc/movies/"
TMP = "/tmp"

fname = "movie_metadata.csv"
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""

    movies = []
    movies_dict = {}

    with open(MOVIE_DATA, newline="") as csvfile:
        myreader = csv.reader(csvfile, delimiter=",")
        for row in myreader:
            movies.append(row)

    # build the dictionary
    movies_dict = defaultdict(list)

    for movie in movies:
        # clean the data, remove the label row
        # and all the entries with an empty director, year
        try:
            notclean = Movie(movie[11], int(movie[23]), float(movie[25]))
        except:
            # the data is not clean, either failed because
            # year is empty or score is a string, discard
            notclean = Movie("", -1, 0)

        if movie[1] in ["director_name", ""]:
            pass
        elif notclean.year < MIN_YEAR:
            pass
        else:
            movies_dict[movie[1]].append(notclean)

    return movies_dict


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""

    total_score = float(0)
    for movie in movies:
        total_score += movie.score
    mean_score = round(total_score / len(movies), 1)

    return mean_score


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""

    result = []

    for director in directors.keys():
        # discard entries with leass than MIN_MOVIES
        if len(directors[director]) >= MIN_MOVIES:
            # get the mean score
            mean_score = calc_mean_score(directors[director])
            result.append((director, mean_score))

    return sorted(result, key=lambda tup: tup[1], reverse=True)
