
numbers = []
n=int(input("Enter the list size: \n "))
for i in range (1,n+1):
    num = input("Enter a number into the list:  ")
    if i==n+1:
        break
    else:
        numbers.append(int(num))


largest = max(numbers)
smallest = min(numbers)


print("The largest number is:", largest)
print("The smallest number is:", smallest)
