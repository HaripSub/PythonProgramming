# tuple creation
employee_names_tuple = ("Alice", 'Bob', 'Charlie', 'Daniel', 'Esther', 'Bob', 'Fedrik')

print("original tuple")
print(employee_names_tuple)

# length of tuple
print(f"length of employee names tuple {len(employee_names_tuple)}")

# count of a particular element in tuple

print(f"count of element - Bob in the tuple: {employee_names_tuple.count('Bob')}")

# assessing element of index 1
print(f"assessing element of index 1: {employee_names_tuple[1]}")

# assessing last element from tuple- negative indexing
print(f"assessing element of index -1: {employee_names_tuple[-1]}")


# slicing operation of tuple
print("slicing operation of tuple")
print(employee_names_tuple[2:5])

print("adding data to a tuple- method 1")
new_employee = ('Gabriel',)
employee_names_tuple += new_employee
print(employee_names_tuple)

print("adding more employees to a tuple")
new_employees = ('Harry', 'Ian')
employee_names_tuple += new_employees
print(employee_names_tuple)

print("adding data to a tuple - method 2 - using lists")
list_from_tuple = list(employee_names_tuple)
list_from_tuple.append('Jensi')
employee_names_tuple = tuple(list_from_tuple)
print(employee_names_tuple)

print("sorting the employee names tuple in ascending order")
sorted_employee_names = sorted(employee_names_tuple)
print(sorted_employee_names)

print("sorting the employee names tuple in descending order")
sorted_employee_names_descending = sorted(employee_names_tuple, reverse=True)
print(sorted_employee_names_descending)
