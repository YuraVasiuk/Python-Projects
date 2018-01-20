import pandas as pd

data = pd.read_csv("movies.csv")

"""
1
"""
# for index, movie in data.iterrows():
#     if movie.year >= 1920 and movie.year < 1930:
#         count += 1

# for year in data.year:
#     if year >= 1920 and year < 1930:
#         count += 1

movies_from_the_20s = data[(data.year >= 1920) & (data.year < 1930)]

count = len(movies_from_the_20s)

rating = movies_from_the_20s.rating.mean()

print("There were {} movies in the 20's".format(count))
print("The average rating from the 20's is: {}".format(rating))

movies_with_rating = data[data.mpaa == " R"]
print(len(movies_with_rating))

"""
2
"""

rating_counts = {}

for rating in data.mpaa:
    if rating in rating_counts:
        # Add one to it
        rating_counts[rating] = rating_counts[rating] + 1
    else:
        rating_counts[rating] = 1

print(rating_counts)


def cleanup_mpaa(old_value):
    new_value = old_value.strip()
    return new_value

data.mpaa_new = data.mpaa.apply(lambda v: v.strip())

def remove_blanks(v):
    if v == "":
        return "Not Rated"
    else:
        return v

data.mpaa_new = data.mpaa_new.apply(remove_blanks)

data.mpaa_new = data.mpaa_new.apply(lambda v: "Not Rated" if v == "" else v)


# value = input("Enter a string: ")
# value = cleanup_mpaa(value)
# print("You entered '{}'".format(value))

print(data.mpaa.value_counts())
print(data.mpaa_new.value_counts())

import pandas as pd

data = pd.read_csv("movies.csv")

rating_counts = {}

for rating in data.mpaa:
    if rating in rating_counts:
        # Add one to it
        rating_counts[rating] = rating_counts[rating] + 1
    else:
        rating_counts[rating] = 1

print(rating_counts)


data.mpaa_new = data.mpaa.apply(lambda v: v.strip())


def remove_blanks(v):
    if v == "":
        return "Not Rated"
    else:
        return v

data.mpaa_new = data.mpaa_new.apply(remove_blanks)

data.mpaa_new = data.mpaa_new.apply(lambda v: "Not Rated" if v == "" else v)


# value = input("Enter a string: ")
# value = cleanup_mpaa(value)
# print("You entered '{}'".format(value))

print(data.mpaa.value_counts())
print(data.mpaa_new.value_counts())

"""
3
"""
# .strip() doesn't change the value of the string, it just returns the new one
# so you have to reassign the variable to equal the new one:
str = "   hello"
str = str.strip()

# similarly with the budget
data.budget = data.budget.apply(lambda v: v.strip())

# Filter to just to ones that have budget
data_with_budget = data[data.budget != "NA"]

# Trouble is that budget column is still a string, even though it has numeric values in that string
# it's like having x and y like this:
x = "13"
y = "7"

# but we want to convert them to ints, like this:
x = int(x)
y = int(y)

# We can do this in one foul swoop, using lambdas and the apply function:
data_with_budget.budget_int = data_with_budget.budget.apply(lambda v: int(v))

count = len(data_with_budget)

print(count)

print(data_with_budget.budget_int.mean())
