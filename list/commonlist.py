list1 = input("Enter a list1 of numbers separated by spaces: ").split()
list1 = [int(num) for num in list1]
list2 = input("Enter a list2 of numbers separated by spaces: ").split()
list2 = [int(num) for num in list2]
common_list = list(set(list1) & set(list2))
print("The common elements  list is :", common_list)
