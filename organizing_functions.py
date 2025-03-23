def factorial(n):
    """
    Recursive function to calculate the factorial of a number.

    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Error: Please enter a non-negative integer.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is: {result:,}")


main()
