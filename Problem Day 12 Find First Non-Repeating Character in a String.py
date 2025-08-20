# Input the string
string = input()

# Convert the string to a list of characters
sl = list(string)

# Flag to check if a non-repeating character is found
present = False

# Check if the string is not empty
if sl:
    for i in sl:
        # If the character appears only once
        if sl.count(i) == 1:
            present = True
            print(i)   # Print the first non-repeating character
            break

# If no non-repeating character found
if present == False:
    print("NO")
