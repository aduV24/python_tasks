# This program prints out a list of movies using a list and the enumerate()
# function
fave_movies = ["Titanic", "Home Alone", "Air force One", "Meet the parents",
               "The Dictator"]
for count, movie in enumerate(fave_movies, 1):
    print(f"movie {count}: {movie}")
