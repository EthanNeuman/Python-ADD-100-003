def two_letter_combinations(characters):
    for first in characters:
        for second in characters:
            yield first + second


def main():
    characters = ['E', 'T', 'H', 'A', 'N']
    for combination in two_letter_combinations(characters):
        print(combination)


main()
