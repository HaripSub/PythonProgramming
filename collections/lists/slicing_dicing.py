whole_numbers = list(range(11))

slice1 = whole_numbers[2:6]
print(slice1)

slice2 = whole_numbers[:5]
print(slice2)

slice3 = whole_numbers[5:]
print(slice3)

odd_numbers = whole_numbers[1:11:2]
print(odd_numbers)

even_numbers = whole_numbers[0:11:2]
print(even_numbers)

reverse_step = whole_numbers[9:3:-1]
print(reverse_step)

reversed_numbers = whole_numbers[::-1]
print(reversed_numbers)

every_third = whole_numbers[::3]
print(every_third)

whole_numbers[2:5] = [20, 30, 40]
print(whole_numbers)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

column = [row[1] for row in matrix]
print(column)

submatrix = [row[:3] for row in matrix[:2]]
print(submatrix)

copied_list = whole_numbers[:]
print(copied_list)










