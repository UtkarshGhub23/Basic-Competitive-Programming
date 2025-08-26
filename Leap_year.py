#WAP to check whether a year is a leap year or not.

year = int(input("Enter year"))

if (year % 4 == 0 ) and (year % 400):
    print(f"{year} is leap year. ")
else:
    print(f"{year} is not leap year")
