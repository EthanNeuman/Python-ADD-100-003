# Start with 99 bottles
bottles = 99

# While there are bottles left
while bottles > 0:
    # singular or plural bottles
    if bottles == 1:
        print(f"{bottles} bottle of beer on the wall")
        print(f"{bottles} bottle of beer")
        print("Take it down, pass it around")
        print("No bottles of beer on the wall!\n")
        bottles -= 1  # Decrease number of bottles to 0
    else:
        print(f"{bottles} bottles of beer on the wall")
        print(f"{bottles} bottles of beer")
        print("Take one down, pass it around")
        bottles -= 1  # Decrease number of bottles
        if bottles > 0:
            print(f"{bottles} bottles of beer on the wall!\n")
