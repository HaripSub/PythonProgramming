from collections import defaultdict

cities = ['Hamburg', 'Berlin', 'Munich', 'Bern', 'Berlin', 'Munich']

count_dict = defaultdict(int)

for item in cities:
    count_dict[item] += 1

print(count_dict)

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi']

grouped_names = defaultdict(list)

for name in names:
    first_letter = name[0]
    grouped_names[first_letter].append(name)

print(grouped_names)

items = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot'), ('fruit', 'apple'),
         ('vegetable', 'beans')]

grouped_items = defaultdict(set)

for category, item in items:
    grouped_items[category].add(item)

print(grouped_items)

shooping_list = [
    ('fruit', 'citrus', 'orange'),
    ('fruit', 'citrus', 'lemon'),
    ('vegetable', 'root', 'beetroot'),
    ('fruit', 'berry', 'strawberry'),
    ('fruit', 'berry', 'blueberry'),
    ('vegetable', 'leafy', 'spinach'),
    ('vegetable', 'root', 'carrot'),
    ('fruit', 'citrus', 'mandarin'),
    ('fruit', 'citrus', 'orange')
]

grouped_items = defaultdict(lambda: defaultdict(list))

for category, subcategory, item in shooping_list:
    grouped_items[category][subcategory].append(item)

print(dict(grouped_items))

berry_count = defaultdict(int)
citrus_count = defaultdict(int)
root_count = defaultdict(int)

for category, subcategory, item in shooping_list:
    if subcategory == 'berry':
        berry_count[item] += 1
    if subcategory == 'citrus':
        citrus_count[item] += 1
    if subcategory == 'root':
        root_count[item] += 1

print(dict(berry_count))

print(dict(citrus_count))

print(dict(root_count))
