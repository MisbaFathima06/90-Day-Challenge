num=int(input("Enter a number: "))

# flag= True            You don’t need flag at all if you’re using return.
                        # return already stops the function and gives the result directly.

def is_prime(num):
    if num<=1:
        return False

    for i in range (2,num):
        if num%i==0:
            return False
        
    else:
        return True
    
if is_prime(num):
    print(f"Entered number {num} is a prime no")
else:
    print(f"Entered number {num} is NOT a prime no")

# If return value was True → print "Prime"
# If return value was False → print "Not prime"


