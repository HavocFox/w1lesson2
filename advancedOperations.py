def create_list(n):
    new_list = []
    i = 1
    while i <= n:
        add_num = i*i               # hope I understood what you wanted
        new_list.append(add_num)
        i = i + 1
    return new_list

# The complexity of this function is O(n) or O(1) because it iterates through a list once.

def merge_lists(list1, list2):
    sorted = list1 + list2
    sorted.sort()
    return sorted

# The complexity of this function is O(n logn) due to the sort function.

# ------------------------------------
# Use the functions:

# Task 1
list_of_squares = create_list(5)    # input whatever number you like
print(list_of_squares)

# Task 2
testlist1 = ['5','2']
testlist2 = ['pekora', 'korone', 'gigi', 'cecelia']     # adjust lists as necessary
merged_lists = merge_lists(testlist1, testlist2)
print(merged_lists)

