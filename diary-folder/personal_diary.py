def main():
    date = input("Enter the date: ")
    time = input("Enter the time: ")
    entry = input("Enter your diary entry: ")
    diary_file = open("diary-folder/diary.txt", "a")

    diary_file.write(f"Date: {date}\n")
    diary_file.write(f"Time: {time}\n")
    diary_file.write(f"Entry: {entry}\n")
    diary_file.write("\n")

    diary_file.close()
    print("Your entry has been saved to diary.txt.")


if __name__ == "__main__":
    main()
