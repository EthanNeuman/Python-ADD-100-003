def main():
    days = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]
    steps = []

    for day in days:
        while True:
            try:
                step_count = int(
                    input(f"How many steps did you take on {day}? "))
                if step_count < 0:
                    print("Please enter a non-negative number.")
                    continue
                steps.append(step_count)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    print("\nSteps recorded:")
    for day, step_count in zip(days, steps):
        print(f"{day}: {step_count}")

    total_steps = sum(steps)
    average_steps = total_steps / len(steps)

    print(f"\nTotal steps: {total_steps}")
    print(f"Average steps: {average_steps:.2f}")


if __name__ == "__main__":
    main()
