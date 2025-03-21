my_list = []

# Append  elements to my_list
my_list = [10, 20, 30, 40]
print("Initial List:", my_list)

# Insert 15 at the second position in the list
my_list.insert(1, 15)
print("List after inserting 15:", my_list)

# Extend my_list with another list
my_list.extend([50, 60, 70])
print("List after extending:", my_list)

# Remove the last element from my_list
my_list.pop()
print("List after removing the last element:", my_list)

# Sort my_list in ascending order
my_list.sort()
print("Sorted List:", my_list)

index = my_list.index(30)
print("Index of 30:", index)