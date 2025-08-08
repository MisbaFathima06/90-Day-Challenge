str_input= input("Enter a string: ")

print(f"The original string is {str_input}")

reverse_str= str_input[::-1]      #Reverses a string

def palindrome(str):
    if str_input==reverse_str:
        return True 
    else:
        return False

result =palindrome(str_input)           
 
if result:                              # By default results to True
    print(f"The string {str_input} is a palindrome")
else:
    print(f"The string {str_input} is  NOT a palindrome")
