# variable declarations

name = input('Enter your name: ')
age = int(input('Enter your age: '))

a = input('Enter first number: ')
b = input('Enter second number: ')

print("...........................................................................................")

print("Functions without arguments")


def print_details():

    print('my name is %s and age is %d' % (name, age))


print("...........................................................................................")

print_details()

print("...........................................................................................")

print("Functions with arguments")

print("...........................................................................................")


def addition(a, b):
    return int(a) + int(b);


def maximum(a, b):
    return max(int(a), int(b));


print(f"The sum of {a} and {b} is {addition(a, b)}")
print(f"The maximum of {a} and {b} is {maximum(a, b)}")

print("...........................................................................................")

print("Default Arguments")

print("...........................................................................................")


def print_color(color="green"):
    print("The color that is adored by me is: " + color)


print_color("Yellow")
print_color("blue")
print_color()

print("------------------------------------------------------------------------------------")

print("Keyword Arguments")

print("------------------------------------------------------------------------------------")


def print_your_details(name, age):
    print(f'my name is {name} and age is {age}')


print_your_details(name="George", age=45)

print_your_details(age=45, name="Sam")

print("------------------------------------------------------------------------------------")

print("Arbitrary Arguments")

print("------------------------------------------------------------------------------------")


def welcome_members(*member_names):
    for team_member in member_names:
        print("Welcome " + team_member + " to the team")


welcome_members("Alice", "Bob", "Charlie", "Daniel")

print("------------------------------------------------------------------------------------")
