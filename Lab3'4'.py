def print_multiplication_table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

def main():
    number = int(input("Enter a number: "))
    print_multiplication_table(number)

if __name__ == "__main__":
    main()
