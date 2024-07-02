dict_1 = {
'pie': 'apple',
'ice_cream': 'moose tracks',
'cobbler': 'peach',
'cake': None
}

dict_2 = {
'dinner': 'turkey',
'ice_cream': 'vanilla',
'appetizer': 'soup',
'cobbler': 'peach'
}

# Task 1
def merge_dicts(dict1, dict2):
    endict = {}
    for key, value in dict1.items():
        if key in dict2:
            endict[key] = [value, dict2[key]]
        else:
            endict[key] = value

    for key, value in dict2.items():
        if key not in dict1:
            endict[key] = value

    return endict

# The time complexity is linear (O(n)).


# Task 2
def find_intersection(dict1, dict2):
    endict = {}
    for key, value in dict1.items():
        if key in dict2 and dict1[key] == dict2[key]:
            endict[key] = value
    return endict

# The time complexity is linear (O(n)).
# -------------------------------------

# Use the functions:

merged = merge_dicts(dict_1, dict_2)
print(merged)

intersect = find_intersection(dict_1, dict_2)
print(intersect)


