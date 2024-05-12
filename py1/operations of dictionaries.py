# Creating a dictionary
days = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7
}

# Accessing elements
print("Monday is day number:", days['Monday'])
print("Saturday is day number:", days['Saturday'])

# Adding a new key-value pair
days['NewDay'] = 8
print("NewDay is day number:", days['NewDay'])

# Updating an existing value
days['Thursday'] = 4.5
print("Updated Thursday:", days['Thursday'])

# Deleting a key-value pair
del days['Friday']
print("After deleting Friday:", days)

# Another way to delete a key-value pair using pop()
removed_value = days.pop('Sunday')
print("Removed Sunday:", removed_value)
print("After popping Sunday:", days)
