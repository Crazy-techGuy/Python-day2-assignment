#Created an empty list
my_list = []

# Appended list items
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserted an item
my_list.insert(1,15)

# Extended the List
new_list = [50, 60, 70]
# my_list = my_list + new_list
my_list.extend(new_list)

# Removed the last item
my_list.pop()

# Sorted the List
my_list.sort()

# Finding the index of 30
index = my_list.index(30)

print(index)
