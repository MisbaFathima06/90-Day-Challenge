'''Swap two variables
2 ways:
1. using temp variables
2. Without temp variable'''

#1. using temp variables

var1= input("Enter a variable: ")#default: It is in string only
var2= input("Enter 2nd wariable: ")
print(f"Before swapping var1 is {var1} and var2 is {var2}")

def swap(v1, v2):
    temp=v1
    v1=v2
    v2=temp
    return v1,v2                #Function arguments are local copies
                                     #Changing them won\’\t affect outside variables unless you return and reassign

var1,var2= swap(var1, var2)

print(f"After swapping var1 is {var1} and var2 is {var2}")


#2. Without temp variable
#This works only if both are numbers, not strings.

n1= int(input("Enter 1st number: "))
n2= int(input("Enter 2nd number: "))

print(f"Before swapping n1 is {n1} and n2 is {n2}")

def swap(n1,n2):
    n1=n1+n2
    n2=n1-n2
    n1=n1-n2
    return n1,n2

n1,n2= swap(n1,n2)      #Reasssigning the values
print(f"After swapping n1 is {n1} and n2 is {n2}")


