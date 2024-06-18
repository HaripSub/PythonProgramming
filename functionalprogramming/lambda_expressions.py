import random
from functools import reduce

numbers = [random.randint(1, 100) for _ in range(5)]

persons = [('Alice', 27, 26000), ('Bob', 29, 33000), ('Charlie', 35, 45000), ('David', 45, 34000)]

# square the numbers in the list of numbers
squared_numbers = list(map(lambda x: x ** 2, numbers))

# filter the even numbers from the list of numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# combining map and filter. Filters the odd numbers from the list and doubles them
doubled_odds = list(map(lambda x: x * 2, filter(lambda x: x % 2 != 0, numbers)))

# adds all the numbers from the list of numbers
sum_all = reduce(lambda x, y: x + y, numbers)

# sorts the persons from the person list by age - second element in list
sorted_persons_by_age = sorted(persons, key=lambda x: x[1])

# sorts the persons from the person list by salary- 3rd element in the list
sorted_persons_by_salary_descending = sorted(persons, key=lambda x: x[2], reverse=True)

# Define a lambda function to perform FizzBuzz logic

fizz_buzz_lambda = lambda x: "FizzBuzz" if x % 3 == 0 and x % 5 == 0 else ("Fizz" if x % 3 == 0
                                                                           else ("Buzz" if x % 5 == 0 else x))
result = list(map(fizz_buzz_lambda, numbers))
