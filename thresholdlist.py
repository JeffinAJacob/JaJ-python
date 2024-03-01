numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
threshold = int(input("Enter a threshold number: "))
lessthres = [num for num in numbers if num < threshold]
print("The list of numbers less than the threshold are:", lessthres)
