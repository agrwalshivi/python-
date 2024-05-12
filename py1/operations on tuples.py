# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# "Updating" a tuple (creating a new tuple)
updated_tuple = my_tuple + (6, 7)
print("Updated tuple:", updated_tuple)

# Deleting a tuple (not elements)
del my_tuple
# Accessing my_tuple now would raise a NameError as it has been deleted
