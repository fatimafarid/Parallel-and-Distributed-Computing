def calculator():
    operation = input("Select operation (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation!")

if __name__ == "__main__":
    calculator()

class StudentDatabase:
    def __init__(self):
        self.students = [
            ("Alice", 22, "Biology"),
            ("Bob", 23, "Mathematics"),
            ("Charlie", 21, "Physics"),
            ("David", 24, "Chemistry")
        ]
        self.student_dict = {}
        self.populate_student_dict()

    def populate_student_dict(self):
        for student in self.students:
            name, age, major = student
            self.student_dict[name] = {"age": age, "major": major}

    def add_student(self, name, age, major):
        self.students.append((name, age, major))
        self.student_dict[name] = {"age": age, "major": major}

    def search_student(self, name):
        if name in self.student_dict:
            return f"{name}: {self.student_dict[name]}"
        else:
            return f"{name} not found."

    def display_students(self):
        for student in self.students:
            print(f"Name: {student[0]}, Age: {student[1]}, Major: {student[2]}")

def main():
    db = StudentDatabase()
    print("Current Students:")
    db.display_students()

    search_name = input("Enter a student's name to search: ")
    result = db.search_student(search_name)
    print(result)

    # Adding a new student
    add_more = input("Do you want to add a new student? (yes/no): ")
    if add_more.lower() == "yes":
        name = input("Enter the student's name: ")
        age = int(input("Enter the student's age: "))
        major = input("Enter the student's major: ")
        db.add_student(name, age, major)
        print(f"Student {name} added successfully!")

    print("\nUpdated Students List:")
    db.display_students()

if __name__ == "__main__":
    main()

#code 3 basic function to add numbers
def add_numbers(num1, num2):
    return num1 + num2

def main():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    result = add_numbers(number1, number2)
    print(f"The sum of {number1} and {number2} is {result}")

if __name__ == "__main__":
    main()
#code 4 making a class with objects and call
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def get_info(self):
        return f"{self.name} is {self.age} years old."

def main():
    # Creating objects of the Dog class
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Max", 5)
    dog3 = Dog("Bella", 2)

    # Calling methods on the objects
    print(dog1.bark())
    print(dog1.get_info())

    print(dog2.bark())
    print(dog2.get_info())

    print(dog3.bark())
    print(dog3.get_info())

if __name__ == "__main__":
    main()

