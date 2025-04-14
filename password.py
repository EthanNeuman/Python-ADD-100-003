def check_password_criteria(password):
    """Returns a list of password issues if criteria are not met."""
    issues = []
    if len(password) < 8 or len(password) > 20:
        issues.append("- Password must be between 8 and 20 characters.")
    if not any(char.isupper() for char in password):
        issues.append("- Password must include at least one uppercase letter.")
    if not any(char.islower() for char in password):
        issues.append("- Password must include at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        issues.append("- Password must include at least one number.")
    if not any(char in "!@#$%&*" for char in password):
        issues.append("- Password must include at least one symbol (!@#$%&*).")
    return issues


def main():
    print("Welcome to the password setup.")

    while True:
        try:
            password = input("Enter your password: ")

            problems = check_password_criteria(password)

            if problems:
                print("\nYour password did not meet the following criteria:")
                for item in problems:
                    print(item)
                print()
                continue

            confirm = input("Re-enter your password to confirm: ")

            if confirm == password:
                print("Password successfully set.")
                break
            else:
                print("Passwords do not match. Please try again.\n")

        except Exception as error:
            print("An error occurred:", error)
            print("Please try again.\n")


main()
