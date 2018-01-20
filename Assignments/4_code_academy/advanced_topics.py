"""
List Comprehension
"""
print("List Comprehension (creating lists)")
# example 1
print("example 1")
squares = [x ** 2 for x in range(1, 11)]
print(squares)
# example 2
print("example 2")
threes_and_fives = [n for n in range(1, 16) if n % 3 == 0 or n % 5 == 0]
print(threes_and_fives)
print()

"""
List Slicing
"""
print("List Slicing")
l = [i ** 2 for i in range(1, 11)]
print(l)
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# [start:end:stride]
print("[start:end:stride]")
print(l[2:9:2])
print(l[::3])

# reverse
print("reverse")
reverse_l = l[::-1]
print(reverse_l)
print(l[::-3])

# some practice
print("Some Practice")
to_21 = list(range(22))
print(to_21)
odds = to_21[0:21:2]
print(odds)
middle_third = to_21[7:14:]
print(middle_third)
# good example of slicing
print("good example of slicing")
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
decrypted = garbled[::-2]
print(decrypted)
print()

"""
Anonymous Functions (lambda)
"""
print("Anonymous Functions")
# example
print("lambda example 1")
my_list = list(range(16))
filtered_list = list(filter(lambda x: x % 3 == 0, my_list))
print(filtered_list)

# example 2
print("lambda example 2")
languages = list(["HTML", "JavaScript", "Python", "Ruby"])
print(list(filter(lambda x: x == "Python", languages)))

# example 3
print("filter + lambda example")
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = list(filter(lambda x: x != "X", garbled))
print(message)

"""
Iterating over Dictionaries
"""
print("Iterating over Dictionaries")
# example 1
movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}
print("example 1")
print(movies.items())




