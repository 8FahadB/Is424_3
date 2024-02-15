numbers = []

for i in range(10):
    value = float(input("Enter value {}: ".format(i + 1)))
    numbers.append(value)

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number

print("The largest number is:", largest_number)
