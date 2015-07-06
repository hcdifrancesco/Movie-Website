# importing webbrowser to open images and videos on  browser.
import webbrowser


class Movie():

    """This Class provides a way to store information about movies"""
    # Class Variable Defining Ratings of Movies.
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # function __init__ with 7 attributes of each movie.
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_actors, movie_oscar_wins):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.starring = movie_actors
        self.oscar_wins = movie_oscar_wins

    # function show_trailer opens youtube trailer of corresponding movie.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
