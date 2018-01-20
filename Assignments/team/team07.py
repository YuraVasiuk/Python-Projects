"""
Team07
Polymorphism
"""
from abc import ABC
from abc import abstractmethod

class Employee(ABC):
    def __init__(self, name = ""):
        self.name = name

    @abstractmethod
    def display(self):
        print("Employee name: {}".format(self.name))

    @abstractmethod
    def get_paycheck(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, name = "", hourly_wage = 0, number_hours = 0):
        super().__init__()
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours = number_hours

    def display(self):
        print("{} - ${}/per hour, ${} paycheck".format(self.name, self.hourly_wage, self.get_paycheck()))

    def get_paycheck(self):
        return self.hourly_wage * self.hours

class SalaryEmployee(Employee):
    def __init__(self, name = "", salary = 0):
        super().__init__()
        self.name = name
        self.salary = salary

    def display(self):
        print("{} - ${}/year, ${:.2f} paycheck".format(self.name, self.salary, self.get_paycheck()))

    def get_paycheck(self):
        return self.salary / 24


def main():
    employees = []

    user_input = ""
    while user_input != "q":
        user_input = input("Input h, s, or q:")
        if user_input == "h":
            hourly_rate = int(input("Input the hourly rate: "))
            name = input("Input the name: ")
            number_hours = int(input("Input the number of hours: "))
            employee = HourlyEmployee(name, hourly_rate, number_hours)
            employees.append(employee)
        if user_input == "s":
            salary = int(input("Input the salary: "))
            name = input("Input the name: ")
            employee = SalaryEmployee(name, salary)
            employees.append(employee)

    for employee in employees:
        employee.display()

if __name__ == "__main__":
    main()



