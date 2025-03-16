# Define time slots
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# Initialize an empty list to store heart rates
heart_rates = []

# Collect heart rate data from the user
for time in time_slots:
    while True:
        try:
            rate = int(
                input(f"Enter your heart rate (in BPM) in the {time}: "))
            if rate > 0:
                heart_rates.append([time, rate])
                break
            else:
                print("Heart rate must be a positive number. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Calculate the average heart rate
average_heart_rate = sum(rate[1] for rate in heart_rates) / len(heart_rates)

# Display results
print("\nHeart Rate Readings:")
for entry in heart_rates:
    print(f"{entry[0]}: {entry[1]} BPM")

print(f"\nAverage heart rate today: {average_heart_rate:.2f} BPM")
