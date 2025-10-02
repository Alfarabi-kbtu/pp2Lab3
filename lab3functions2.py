"""
Check if a single movie has IMDB > 5.5

def is_above_55(movie):
    return movie["imdb"] > 5.5


print(is_above_55(movies[0]))   
print(is_above_55(movies[7]))

""" 
"""
Return sublist of movies with IMDB > 5.5

def above_55_movies(movies):
    return [m for m in movies if m["imdb"] > 5.5]

print([m["name"] for m in above_55_movies(movies)])


"""

"""
Return movies by category

def movies_by_category(movies, category):
    return [m for m in movies if m["category"].lower() == category.lower()]

print([m["name"] for m in movies_by_category(movies, "Romance")])

"""

"""
Compute average IMDB score of a list of movies

def average_imdb(movies):
    if not movies:  
        return 0
    return sum(m["imdb"] for m in movies) / len(movies)


print(average_imdb(movies))
"""

"""
Compute average IMDB score for a category

def average_imdb_by_category(movies, category):
    filtered = [m for m in movies if m["category"].lower() == category.lower()]
    return average_imdb(filtered)


print(average_imdb_by_category(movies, "Romance"))


"""