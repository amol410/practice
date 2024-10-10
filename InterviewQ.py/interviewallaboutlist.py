# we can change elements in list
# It can store diff data types
random_list = [17, 5.5, 17, "This is an element in a list", "Hello!", True, None]
print(random_list)

random_list[0] = 10
print("List after updation:", random_list)

# we cant change elements in tuple
# It can also store diff data types
random_tuple = (12, "How is your Python Journey going?", False, True, 25.6, 25.6)
print(random_tuple)

# comment the line below to remove the error
random_tuple[0] = 20
print(random_tuple)


# Adds element x to the end of the list. list.append(x)
python_versions = ["Python 2", "Python 3"]
python_versions.append("Python 3.11")

print(python_versions)


# Appends elements from the iterable to the end of the list. list.extend(iterable)
python_modules = ["NumPy", "Pandas"]

additional_modules = ["Matplotlib", "scikit-learn"]
python_modules.extend(additional_modules)

print(python_modules)

# Inserts element x at index i in the list. list.insert(index, element)
programming_languages = ["C", "Java", "Python", "Ruby"]
programming_languages.insert(1, "C++")

print(programming_languages)

# Removes the first occurrence of element x from the list. list.remove(x)
frameworks = ["Django", "Flask", "Pyramid", "Flask"]
frameworks.remove("Flask")

"""Removes and returns the element at index i, 
or the last element if i is not specified.""" # list.pop([i])

web_frameworks = ["Django", "Flask", "Pyramid", "FastAPI"]
removed_framework = web_frameworks.pop(2)

print(web_frameworks)

# Removes all elements from the list. list.clear()
scripting_languages = ["Python", "Ruby", "Perl"]
scripting_languages.clear()

print(scripting_languages)

# Returns the index of the first occurrence of element x. list.index(x)
languages = ["C", "C++", "Python", "Java", "Python"]
python_index = languages.index("Python")

print(python_index)

# Returns the number of occurrences of element x in the list. list.count(x)
version_numbers = [2, 3, 3, 3, 3, 3, 3, 3, 3, 3]
python3_count = version_numbers.count(3)

print(python3_count)

# list.sort(*, key=None, reverse=False)
# Sorts the elements of the list in ascending order.
numeric_versions = [2.7, 3.0, 3.6, 3.7, 3.8, 3.9]
numeric_versions.sort()

print(numeric_versions)

# list.reverse()
# Reverses the order of elements in the list.
libraries = ["NumPy", "Pandas", "Matplotlib", "Scikit-Learn"]
libraries.reverse()

print(libraries)

# list.copy()
# Returns a shallow copy of the list.
original_list = ["Python", "is", "so" , "cool"]
copied_list = original_list.copy()

print(copied_list)


# dictionary adding new key:value pair
random_dict = {"key1": "value1", "key2": 42, "key3": True}
print(random_dict)

random_dict["new_key"] = "Hope you're learning well!"
print("Dictionary after updation:", random_dict)

# Set contains only unique elements even if you add 1 it won't work
random_set = {1, 2, 3, 4}
print(random_set)

random_set.add(1)
print("Set after updation: ", random_set) 

# blank set can be defined like below
ran_set = set()

ran_set.add(1)
print("Set after updation: ", random_set)