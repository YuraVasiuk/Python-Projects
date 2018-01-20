import pandas
import matplotlib.pyplot as plt

# get all the data
movies_data = pandas.read_csv("movies.csv")

"""
#1 Calculate the mean and median values for rating
"""
print("#1")
rating_mean = round(movies_data.rating.mean(), 2)
print("The mean for all movies rating is {}".format(rating_mean))

rating_median = round(movies_data.rating.median(), 2)
print("The median for all movies ratings is {}".format(rating_median))

"""
#2 According to this dataset, what was the first year that the "PG-13" MPAA rating was issued?
"""
print("#2")
first_year = 2017
rated_PG_13_movies = movies_data[movies_data.mpaa == " PG-13"]
years = rated_PG_13_movies.year
for year in years:
    if year < first_year:
        first_year = year

print("The first year that the PG-13 MPAA rating was issued is {}".format(first_year))
print()

"""
#3 For all the movies that have an MPAA Rating (e.g., "PG", "R", etc.), 
produce a bar chart showing the number of movies in each of these categories
"""
print("#3")
rates = set()
rates.update(movies_data.mpaa)
print("Here is the set of rates: {}".format(rates))

movies_R = 0
movies_PG = 0
movies_NC_17 = 0
movies_PG_13 = 0
movies_not_rated = 0
rates = movies_data["mpaa"]

for rate in rates:
    if rate == " PG":
        movies_PG += 1
    if rate == " NC-17":
        movies_NC_17 += 1
    if rate == " PG-13":
        movies_PG_13 += 1
    if rate == " ":
        movies_not_rated += 1
    if rate == " R":
        movies_R += 1

print("PG movies: {}".format(movies_PG))
print("NC movies: {}".format(movies_NC_17))
print("PG-13 movies: {}".format(movies_PG))
print("R movies: {}".format(movies_R))
print("not rated movies: {}".format(movies_not_rated))
print()

#data = [movies_NC_17, movies_PG, movies_PG_13, movies_R, movies_not_rated]
#plt.plot(data)
#plt.show()

"""
#4 Produce a graph showing the number of movies released each year
"""
print("#4")

# all possible years (113 altogether)
years = set()
years.update(movies_data.year)
print("There are {} movie production years".format(len(years)))

# all years for all movies (same number with the number of movies)
movie_years = movies_data.year

# the dictionary to put in years and counted movies number
movies_per_year = {}
for y in years:
    # make the dictionary have 113 items
    movies_per_year.update({y : 0})

# go through all years for all movies
for y in movie_years:
    # for each year add 1 to the number of movies in the above created dictionary
    # 1) get the current number and add 1
    num = movies_per_year.get(y)
    num += 1
    # 2) update the dictionary item for the current year
    movies_per_year.update({y : num})

"""
# do the counts and update the dictionary
for y in years:
    for year in movie_years:
        if y == year:
            current_number = movies_per_year.get(y)
            movies_per_year.update({y : current_number + 1})
"""
print("Year: Number of Movies")
for m in movies_per_year:
    print("{} -- {}".format(m, movies_per_year.get(m)))

# get the data for graphing
years = []
for i in movies_per_year.keys():
    years.append(i)

movies_number = []
for i in movies_per_year.values():
    movies_number.append(i)
# and graph
plt.plot(years, movies_number)
plt.show()














