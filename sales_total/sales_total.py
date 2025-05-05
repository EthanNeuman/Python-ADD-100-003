def main():
    try:
        with open("sales_total/sales_total.txt", "r") as file:
            total = 0.0
            count = 0
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line:
                    try:
                        amount = float(cleaned_line)
                        print(f"{amount:,.2f}")
                        total += amount
                        count += 1
                    except ValueError:
                        print(
                            f"Warning: Could not convert line '{cleaned_line}' to a number.")

            print()
            print(f"Total: {total:,.2f}")
            print(f"Number of entries: {count}")
            if count > 0:
                average = total / count
                print(f"Average: {average:,.2f}")
            else:
                print("Average: no valid entries")

    except FileNotFoundError:
        print("Error: sales_totals.txt file not found. .")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
