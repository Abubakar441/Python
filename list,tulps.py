# Create a list of cars
cars = ["corola", "xli", "gli", "gli"]

# Print the item at index 1 (second item)
print(cars[1])

# Add a new item at the end of the list
cars.append("city")
print(cars)

# Remove the first occurrence of "xli"
cars.remove("xli")
print(cars)

# Insert "alto" at index 2
cars.insert(2, "alto")
print(cars)

# Add multiple items to the end of the list
cars.extend(["markx", "crown"])
print(cars)

# Remove the item at index 1
cars.pop(1)
print(cars)

# Find the index of the first occurrence of "gli"
print(cars.index("gli"))

# Count how many times "gli" appears in the list
print(cars.count("gli"))

# ---------------------------
# Other useful list methods
# ---------------------------

# Print the total number of items
print(len(cars))

# Sort the list alphabetically
cars.sort()
print(cars)

# Reverse the current order of the list
cars.reverse()
print(cars)

# Make a copy of the list
new_cars = cars.copy()

len(fruits)
max(numbers)
min(numbers)
sum(numbers)
print(new_cars)

# Clear all items from the copied list
new_cars.clear()
print(new_cars)   # Output: []

# Create a dictionary
info = {
    "name": "ali",
    "class": "9th",
    "city": "rawalpindi"
}

# Print the entire dictionary
print(info)

# Print the value of the "name" key
print(info["name"])

# Print the value of the "city" key
print(info["city"])

# Get the value of "class" using get() (safer than [])
print(info.get("class"))

# Update the value of "class"
info["class"] = "10th"

# Print the updated class
print(info.get("class"))

# Add a new key-value pair
info["cars"] = "grande"

# Print the updated dictionary
print(info)

# Remove the "name" key
info.pop("name")

# Print the dictionary after removing "name"
print(info)

# Print all keys
print(info.keys())

# Print all values
print(info.values())

# Print all key-value pairs
print(info.items())

# Update the value of the "city" key
info.update({"city": "pindi"})

# Print the updated dictionary
print(info)

# Remove the last inserted key-value pair
info.popitem()

# Print the final dictionary
print(info)
