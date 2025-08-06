year=int(input("Enter a year: "))

def leap_or_not(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        print(f"Entered year {year} is a leap year ")
    else:
        print(f"Entered year {year} is not  a  leap year ")
    
    return year

year= leap_or_not(year)
