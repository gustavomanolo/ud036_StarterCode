
class Movie():
    """This class provides a way to create instances of type 'Movie' with the
    following properties:

    Attributes:
        title: The title of the movie
        poster_image_url: A valid URL to an image of the movie's poster
        trailer_youtube_url: A valid Youtube's URL for the movie's trailer
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Inits Movie class with the attributes described above."""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
