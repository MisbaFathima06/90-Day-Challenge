num=int(input("Enter the number: "))

def increasing(num):
    for i in range(num):
        for j in range(i+1):   #increasing
            print("*" ,end=" ")
        print()

increasing(num)
