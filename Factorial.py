import math
print(math.factorial(5))

# 2. Using loop

num= int(input("Enter the number: "))

def factorial(num):
    result=1        #Start with 1 because factorial multiplies from 1 upwards

    for i in range(1,num+1):
        result=result*i     #Multiply result by each i

    return result

num=factorial(num)
print(num)

#  3. Recursion

def recursion(num):
    #Base case: factorial of 0 or 1 is 1
    if num==0 or num==1:
        return 1
    else:
        fact= num* recursion(num-1)
    
    return fact

fact=recursion(num)
print(fact)
