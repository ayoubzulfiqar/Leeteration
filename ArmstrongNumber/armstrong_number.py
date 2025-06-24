def is_armstrong(number):
    num_str = str(number)
    n = len(num_str)
    armstrong_sum = 0
    for char_digit in num_str:
        digit = int(char_digit)
        armstrong_sum += digit ** n
    return armstrong_sum == number

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            print("Please enter a non-negative number.")
        else:
            if is_armstrong(num):
                print(f"{num} is an Armstrong number.")
            else:
                print(f"{num} is not an Armstrong number.")
    except ValueError:
        print("Invalid input. Please enter an integer.")