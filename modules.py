import random


def main():
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Guess the number between 1 and 100.")

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        difference = abs(secret_number - guess)

        if guess == secret_number:
            print(f"Correct! You guessed the number in {attempts} attempts.")
        else:
            if difference <= 5:
                print("Very Hot")
            elif difference <= 15:
                print("Hot")
            elif difference <= 25:
                print("Cool")
            else:
                print("Cold")


if __name__ == "__main__":
    main()
