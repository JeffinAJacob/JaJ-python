numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
even_numbers = [num for num in numbers if num % 2 == 0]
even_numbers.sort()
print("The list of even numbers in ascending order are:", even_numbers)
