import media
import fresh_tomatoes

# Create instances of "Movie" class
shawshank = media.Movie(
    "The Shawshank Redemption",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_UY1200_CR88,0,630,1200_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

godfather = media.Movie(
    "The Godfather",
    "https://lunkiandsika.files.wordpress.com/2011/11/the-godfather-alternative-poster-1972-01.png",  # noqa
    "https://www.youtube.com/watch?v=sY1S34973zA")

dark_knight = media.Movie(
    "The Dark Knight",
    "https://fanartexhibit.files.wordpress.com/2009/01/oscars_2.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

schindler_list = media.Movie(
    "Schindler's List",
    "https://fanart.tv/fanart/movies/424/movieposter/schindlers-list-52e73e7ba8e35.jpg",  # noqa
    "https://www.youtube.com/watch?v=gG22XNhtnoY")

good_bad_ugly = media.Movie(
    "The Good, The Bad and The Ugly",
    "http://img.moviepostershop.com/the-good-the-bad-and-the-ugly-movie-poster-1966-1010415095.jpg",  # noqa
    "https://www.youtube.com/watch?v=WCN5JJY_wiA")


"""Create an open the HTML using "open_movies_page" function from
"fresh_tomatoes" library"""
movies = [shawshank, godfather, dark_knight, schindler_list, good_bad_ugly]
fresh_tomatoes.open_movies_page(movies)
