# Create a list representing 20 seats, numbered 1 to 20
available_seats = list(range(1, 21))

# Display available seats to the customer


def display_seats():
    print("\nAvailable Seats:", available_seats)


#  customer to select a seat
while True:
    display_seats()
    try:
        choice = int(input("Enter the seat number to book (or '0' to exit): "))

        if choice == 0:
            print("Thank you for using the ticket booking system. Goodbye!")
            break
        elif choice in available_seats:
            available_seats.remove(choice)
            print(f"Seat {choice} booked successfully!")
        else:
            print(
                "Invalid selection! Seat is either already booked or does not exist. Try again.")
    except ValueError:
        print("Invalid input! Please enter a valid seat number.")
