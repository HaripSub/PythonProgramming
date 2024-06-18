import math
from functools import reduce

# adds 2 numbers using lambda
add = lambda x, y: x + y

# find the maximum of 2 numbers using lambda
maximum_two_numbers = lambda a, b: a if a > b else b

# factorial of a number using lambda and math library
factorial_num = lambda num: math.factorial(num)

# square a number using lambda and math library
square_num = lambda n: int(math.pow(n, 2))

# find the maximum from a list of numbers using lambda
find_max_numbers_list = lambda numbers: reduce(lambda a, b: a if a > b else b, numbers)

# find the sign of a given number using lambda
check_sign = lambda x: 'Positive number' if x > 0 else ('Negative number' if x < 0 else 'Number is Zero')

# check if the given number is prime or not prime using lambda
is_prime = lambda number: f"The {number} is prime" if number > 1 and all(number % i != 0 for i in
                                                                         range(2, int(math.sqrt(
                                                                             number)) + 1)) \
                                                                else f"The {number} is not prime"

