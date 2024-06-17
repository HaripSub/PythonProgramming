import math
from functools import reduce

add = lambda x, y: x + y

maximum_two_numbers = lambda a, b: a if a > b else b

factorial_num = lambda num: math.factorial(num)

square_num = lambda n: int(math.pow(n, 2))

find_max_numbers_list = lambda numbers: reduce(lambda a, b: a if a > b else b, numbers)
