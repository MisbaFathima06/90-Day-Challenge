#1. Using loop

string= input("Enter a string: ")    # Bydefault: Returns a string
print(f"Original String is {string}")
reversed_str=""                     #empty string to store the reversed result

for char in string:
    reversed_str= char+ reversed_str   #traverse through each char in string and gets added up into this
                                    #*IMP*= adds character to the front, not end

print(f"Reversed String is {reversed_str}")

#2. Using slicing

string= input("Enter a string: ")    
print(f"Original String is {string}")

reversed_str= string[::-1]          # [start:stop:step] → step -1 means reverse
print(f"Reversed String is {reversed_str}")


