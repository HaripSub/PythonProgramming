from collections import Counter

# Counting characters in a string
string = "abracadabra"
string_elements_counter = Counter(string)
print(string_elements_counter)

# Counting words in a list
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruits_counter = Counter(fruits)
print(fruits_counter)


# Updating counts with another iterable
counter = Counter("welcome")
counter.update("to")
print(counter)

# Updating counts with another Counter
counter2 = Counter("python")
counter.update(counter2)
print(counter)


