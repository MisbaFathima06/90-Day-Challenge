num=int(input("Enter the binary number: "))

def replace(num):
    str_input=str(num)        #converted number to string
    replaced_str=str_input.replace("0","1")
    replaced_int=int(replaced_str)      #converted back to integer

    return replaced_int
  
num=replace(num)
print(f"The replaced num is {num}")