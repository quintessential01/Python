# Homeworks:
## Dictionary Exercises

### 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.
first_dict = {'USA': 'Washington D.C.', 'SWEDEN': 'Stockholm', 'Australia': 'Canberra'}
# Ascending order
asc_dict = dict(sorted(first_dict.items(), key=lambda item: item[1]))
print("Ascending order:", asc_dict)
# Descending order
desc_dict = dict(sorted(first_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", desc_dict)

### 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.

# **Sample Dictionary:**
# ```python
# {0: 10, 1: 20}
# ```

# **Expected Result:**
# ```python
# {0: 10, 1: 20, 2: 30}
# ```

### First option to add a key to a dictionary
sample_dict = {0:10, 1:20}
sample_dict[2] = 30
print("Updated Dictionary:", sample_dict)

### Second option to add a key to a dictionary
sample_dict = {0:10, 1:20}
sample_dict.update({2: 30})
print("Updated Dictionary:", sample_dict)
### 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.

# **Sample Dictionaries:**
# ```python
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
# ```

# **Expected Result:**
# ```python
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# ```

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dic = {**dic1, **dic2, **dic3}
print("Concatenated Dictionary:", new_dic)

### Second option to concatenate multiple dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dic2 = dic1 | dic2 | dic3
print("Concatenated Dictionary2:", new_dic2)
### 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form `(x, x*x)`.

# **Sample Dictionary (n = 5):**
# ```python
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# ```

n = 5
squared_dict = {x: x*x for x in range(1, n+1)}
print("Dictionary with squares:", squared_dict)
### 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

# **Expected Output:**
# ```python
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# ```
squared_dict_15 = {x: x*x for x in range(1, 16)}
print("Dictionary of squares from 1 to 15:", squared_dict_15)
## Set Exercises

### 1. Create a Set
# Write a Python program to create a set.
my_set = {1, 2, 3, 4, 5}
print("Created Set:", my_set)

### 2. Iterate Over a Set
# Write a Python program to iterate over sets.
for item in my_set:
    print("Set item:", item)

### 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.
my_set.add(6)
print("Set after adding an item:", my_set)

### 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.
my_set.remove(3)
print("Set after removing an item:", my_set)

### 5. Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.
item_to_remove = 4
if item_to_remove in my_set:
    my_set.remove(item_to_remove)
