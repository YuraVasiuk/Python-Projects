##############
"""
Set
"""
rsvp = set()

rsvp.add("Pepe")
rsvp.add("James")
rsvp.add("John")

name = input("Enter a name: ")

if name in rsvp:
    print("They are in the list")
else:
    print("Not in the list")

############
"""
Dictionary
"""
race_times = dict()
# shorthand notation for the same thing:
# race_times = {}

race_times["Mark"] = 24
race_times["John"] = 15

name = input("Whose time? ")
time = race_times[name]

print("The {}'s time is: {}".format(name, time))

#############
"""
List comprehension
"""
# basic syntax
doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]
print(doubles_by_3)

even_squares = [y**2 for y in range(1, 11) if (y**2) % 2 == 0]
print(even_squares)

nums = []
for i in range(1, 11):
    if i % 2 == 0:
        nums.append(i)
print(nums)

nums2 = [i for i in range(1, 101) if i % 2 == 0]
print(nums2)


powersof2 = [2 ** x for x in range(1, 100)]
print(powersof2)


words = ["cat", "bitter", "scrumptious", "is", "delicious", "cold",
         "spider", "cash", "cache", "bacon", "money", "pokemon", "go"]
print(words)

small_words = [word for word in words if len(word) <= 5]
print(small_words)

c_words = [word for word in words if word[0] == "c"]
print(c_words)

any_c_words = [word for word in words if "c" in word and len(word) >=5]
print(any_c_words)

#c_words = [word for word in words if is_edible(word)]
