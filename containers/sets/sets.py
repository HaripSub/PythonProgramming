print("creating set- Using curly braces")
fruits = {"orange", "grapes", "mango"}
print(fruits)

print("creating set - Using the set() function")
integer_list = []
for i in range(1, 6):
    integer_list.append(i)
numbers = set(integer_list)
print(numbers)

print("Adding a single element")
fruits.add("apple")
print(fruits)

print("Adding multiple elements")
fruits.update(["peach", "banana"])
print(fruits)

print("Removing an element")
fruits.remove("banana")
print(fruits)

print("Discarding an element (no error if element not found- pineapple)")
fruits.discard("pineapple")
print(fruits)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"set1: {set1}")
print(f"set2: {set2}")

print("Union (elements in either set)")
union_set = set1.union(set2)
print("Union:", union_set)

print("Intersection (elements in both sets)")
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

print("Difference (elements in set1 but not in set2)")
difference_set = set1.difference(set2)
print("Difference:", difference_set)

print("Symmetric Difference (elements in either set, but not both)")
sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff_set)



