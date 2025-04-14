# Python String Methods Practice

# TODO: Use the capitalize() method to capitalize the first letter of the string.
# Example: "python" should become "Python".
string1 = "python"
print(string1.capitalize())

# TODO: Use the center() method to center the string within a given width.
# Example: "python" centered in a width of 10 should return " python  ".
string2 = "python"
print(string2.center(10))

# TODO: Use the endswith() method to check if the string ends with a specified substring.
# Example: Check if "python" ends with "on".
string3 = "python"
print(string3.endswith("on"))

# TODO: Use the find() method to get the position of the first occurrence of a substring in the string.
# Example: Find the index of "th" in the string "python".
string4 = "python"
print(string4.find("th"))

# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric (letters or numbers only).
# Example: Check if "python3" contains only alphanumeric characters.
string5 = "python3"
print(string5.isalnum())

# TODO: Use the isalpha() method to check if all characters in the string are alphabetic (letters only).
# Example: Check if "python" contains only letters.
string6 = "python"
print(string6.isalpha())

# TODO: Use the islower() method to check if all characters in the string are lowercase.
# Example: Check if "python" is all lowercase.
string7 = "python"
print(string7.islower())

# TODO: Use the isspace() method to check if the string contains only whitespace characters.
# Example: Check if " " (a single space) contains only whitespace.
string8 = " "
print(string8.isspace())

# TODO: Use the isupper() method to check if all characters in the string are uppercase.
# Example: Check if "PYTHON" is all uppercase.
string9 = "PYTHON"
print(string9.isupper())

# TODO: Use the join() method to join the items in an iterable with a specified separator string.
# Example: Join the list ["Python", "is", "fun"] using "-" to get "Python-is-fun".
iterable1 = ["Python", "is", "fun"]
separator = "-"
print(separator.join(iterable1))

# TODO: Use the lower() method to convert all characters in the string to lowercase.
# Example: Convert "PYTHON" to "python".
string10 = "PYTHON"
print(string10.lower())

# TODO: Use the lstrip() method to remove leading whitespace characters from the string.
# Example: Remove the space at the beginning of " python" to get "python".
string11 = " python"
print(string11.lstrip())

# TODO: Use the rstrip() method to remove trailing whitespace characters from the string.
# Example: Remove the space at the end of "python " to get "python".
string12 = "python "
print(string12.rstrip())

# TODO: Use the replace() method to replace all instances of one substring with another.
# Example: Replace "python" with "snake" in the string "I love python".
string13 = "I love python"
print(string13.replace("python", "snake"))

# TODO: Use the rfind() method to find the highest index of a specified substring in the string.
# Example: Find the last index of "n" in the string "python".
string14 = "python"
print(string14.rfind("n"))

# TODO: Use the split() method to split the string at a specified separator and return a list of substrings.
# Example: Split the string "python-is-fun" using "-" to get ["python", "is", "fun"].
string15 = "python-is-fun"
print(string15.split("-"))

# TODO: Use the startswith() method to check if the string starts with a specified substring.
# Example: Check if "python" starts with "py".
string16 = "python"
print(string16.startswith("py"))

# TODO: Use the strip() method to remove both leading and trailing whitespace characters from the string.
# Example: Remove spaces from the beginning and end of " python " to get "python".
string17 = " python "
print(string17.strip())

# TODO: Use the swapcase() method to swap the case of each character in the string.
# Example: Convert "Python" to "pYTHON".
string18 = "Python"
print(string18.swapcase())

# TODO: Use the title() method to convert the first character of each word to uppercase.
# Example: Convert "python is fun" to "Python Is Fun".
string19 = "python is fun"
print(string19.title())

# TODO: Use the upper() method to convert all characters in the string to uppercase.
# Example: Convert "python" to "PYTHON".
string20 = "python"
print(string20.upper())
