
largest = float('-inf')
second_largest = float('-inf')
third_largest = float('-inf')


for _ in range(3):
    num = float(input("Enter a number: "))
    if num > largest:
        third_largest = second_largest
        second_largest = largest
        largest = num
    elif num > second_largest:
        third_largest = second_largest
        second_largest = num
    elif num > third_largest:
        third_largest = num

# Check if there are at least 3 numbers in the list
if largest == float('-inf'):
    print("There are less than 3 numbers in the list.")
else:
    # Print the third largest number
    print("The third largest number is:", third_largest)
