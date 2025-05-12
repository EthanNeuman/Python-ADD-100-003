# calculate a person's age in: Years, months, weeks, days
# 30.41 days in a month
# 7 days in a week

from datetime import datetime


def main():
    print("\n\n")
    try:
        today = datetime.today()
        birth_year = int(input("What year were you born?  "))
        month = int(
            input("What month were you born (as a number. May would be 5)?  "))
        day = int(input("What day of the month were you born?  "))
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output)

        delta = today - birthday
        print(f'Difference is {delta.days} days')

        delta_years = delta.days / 365.2425
        print(f'You are approximately {delta_years:.2f} years old')

        delta_months = delta.days / 30.41
        print(f'You are approximately {delta_months:.2f} months old')

        delta_weeks = delta.days / 7
        print(f'You are approximately {delta_weeks:.2f} weeks old')

        delta_hours = delta.days * 24
        print(f'You are approximately {delta_hours:.2f} hours old')

        delta_minutes = delta_hours * 60
        print(f'You are approximately {delta_minutes:.2f} minutes old')

    except Exception as e:
        print(f"oooooops!!!: {e}")
        main()


main()
