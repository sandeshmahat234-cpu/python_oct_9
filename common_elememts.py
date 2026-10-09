list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 50, 70, 80, 90]
common_elements = list(set(list1) & set(list2))
print("Common elements:", common_elements)
print("Values only in list1:", list(set(list1) - set(list2)))
print("Values only in list2:", list(set(list2) - set(list1)))