# Unique Number Sorter
# Ask the user to enter numbers one by one (let them enter 0 to stop input).
# Store all unique numbers in a list (ignore duplicates).
# Once the user enters 0, sort the list in ascending order and print the result.

Numlist = []
print("Unique Number Sorter")
print("Enter numbers one by one. Enter 0 to stop the program")

while True:
    print("Enter a number (0 to stop): ")
    inputnum = int(input())
    if inputnum == 0:               # Validate number is not 0
        break
    if inputnum in Numlist:         # Skip duplicates
        continue
    Numlist.append(inputnum)       # Add input to list
    #print(inputnum)

Numlist.sort()
print(Numlist)


# Need to add error Handling