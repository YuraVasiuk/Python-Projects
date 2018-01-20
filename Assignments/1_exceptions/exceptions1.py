try:
    num = int(input("Please enter a number: "))
    result = 10 / num
    print(result)
except ValueError as theProblem:
    print("ValueError happened")
    print("Details:")
    print(theProblem)
except:
    print("Something else happened")

print("The rest of the program is running here.")