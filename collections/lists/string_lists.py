dry_fruits_list = ["cashew", "almond", "pistachio", "dates"]

capitalized_dry_fruits_list_sorted = sorted([fruit.capitalize() for fruit in dry_fruits_list])

# insert a new dry fruit in the list at position 2 and sort it again

capitalized_dry_fruits_list_sorted.insert(2, "walnut".capitalize())

capitalized_dry_fruits_list_sorted_with_new_element = sorted(capitalized_dry_fruits_list_sorted)

# append a new dry fruit in the list at position and sort it again in descending order

capitalized_dry_fruits_list_sorted.append("Pecan")

capitalized_dry_fruits_list_appended_sorted = sorted(capitalized_dry_fruits_list_sorted, reverse=True)


new_nuts_list = ["Peanut", "Hazelnut", "Macadamia", "Coconut"]

capitalized_dry_fruits_list_appended_sorted.extend(new_nuts_list)

sorted_extended_dry_fruits_list = sorted(capitalized_dry_fruits_list_appended_sorted)

# removing the last element from the list

sorted_extended_dry_fruits_list.pop()










