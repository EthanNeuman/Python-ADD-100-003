# enter five names and store them in a list
names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

# Implement Bubble Sort to sort the list


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


# Sort the names list
bubble_sort(names)

# Reverse the sorted list using a Python list method
reversed_names = names.copy()
reversed_names.reverse()

# Print the sorted and reversed lists
print("\nSorted Names:", names)
print("Reversed Names:", reversed_names)
