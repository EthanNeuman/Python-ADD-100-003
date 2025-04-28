class NotNumericError(Exception):
    pass


def get_number_input():
    while True:
        try:
            user_input = input("Please enter a number: ")
            if not user_input.isnumeric():
                raise NotNumericError(
                    "Invalid input! You must enter a valid number.")

            number = int(user_input)

        except NotNumericError as e:
            print(f"Error: {e}")

        else:
            print(f"Thank you! You entered the number: {number}")
            break

        finally:
            print("Execution completed for this input attempt.\n")


def main():
    get_number_input()


main()
