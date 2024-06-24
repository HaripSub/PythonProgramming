class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age  # Attribute

    def print_details(self):
        print(f"The given person name is: {self.name} and is of age: {self.age}")


# Creating an object
name = input("Enter the name of the person ")
age = int(input("Enter the age of the person "))

person1 = Person(name, age)

# Accessing attributes and methods
print(person1.name)
print(person1.age)
person1.print_details()
