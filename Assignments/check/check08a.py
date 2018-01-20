"""
Check08a
Yurii Vasiuk
Getters and Setters
"""
class GPA():
    def __init__(self):
        self.gpa = 0.0

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        if gpa < 0:
            self.gpa = 0.0
        elif gpa > 4:
            self.gpa = 0.0
        else:
            self.gpa = gpa

    def get_letter(self):
        if self.gpa < 1.0:
            return "F"
        elif self.gpa < 2.0:
            return "D"
        elif self.gpa < 3.0:
            return "C"
        elif self.gpa < 4.0:
            return "B"
        else:
            return "A"

    def set_letter(self, gpa):
        if gpa == "F":
            self.gpa = 0.0
        elif gpa == "D":
            self.gpa = 1.0
        elif gpa == "C":
            self.gpa = 2.0
        elif gpa == "B":
            self.gpa = 3.0
        elif gpa == "A":
            self.gpa = 4.0

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

if __name__ == "__main__":
    main()
