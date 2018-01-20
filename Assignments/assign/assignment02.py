"""
Assignment02
"""
# standard procedure for opening the file
fileName = input("Please enter the data file: ")
file = open(fileName, "r")

# varibles to be used in the loop
firstLine = True
lowest = 1.0
highest = 0.0
lowestCompanyName = " "
highestCompanyName = " "
rateSum = 0.0
countCompanies = 0

# loop through the file reading it and working on the data
for line in file:
    # skip the first line
    if firstLine == True:
        firstLine = False
        pass
    # work on the data
    else:
        data = line.split(",")
        rate = float(data[6])
        if rate < lowest:
            lowest = rate
            lowestCompanyName = data[2] + " (" + data[0] + ", " + data[3] + ")"
        if rate > highest:
            highest = rate
            highestCompanyName = data[2] + " (" + data[0] + ", " + data[3] + ")"
        rateSum += rate
        countCompanies += 1

averageRate = rateSum / countCompanies

print("\nThe average commercial rate is: {}".format(averageRate))
print("\nThe highest rate is:\n{} - ${}".format(highestCompanyName, highest))
print("\nThe lowest rate is:\n{} - ${}".format(lowestCompanyName, lowest))
