# Ask the user for their age and convert the input to an integer
age = int(input("How old are you? "))

#  if the user is old enough to drive (age 16 or older)
if age >= 16:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")

# if the user can vote (age 18 or older)
if age >= 18:
    print("You can vote.")
else:
    print("You are not old enough to vote.")

# if the user can legally buy alcohol (age 21 or older)
if age >= 21:
    print("You can buy alcohol legally.")
else:
    print("You cannot buy alcohol legally.")

# if the user is eligible for a senior discount (age 65 or older)
if age >= 65:
    print("You are eligible for a senior discount.")
else:
    print("You are not eligible for the senior discount.")
