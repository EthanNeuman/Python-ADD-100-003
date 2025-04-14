def main():
    book_list = []

    count = 0

    print("Please enter 10 of your favorite book titles.\n")

    while count < 10:
        title = input(f"Book {count + 1}: ")
        book_list.append(title.title())
        count += 1

    books_sorted = sorted(book_list)

    print("\nYour book titles in alphabetical order:\n")
    for book in books_sorted:
        print(book)


main()
