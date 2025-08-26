# 10.⁠ ⁠WAP to accept a number from 1 to 7 and display the name of the day, like 1 for Sunday, 2 for Monday, etc.


a = int(input("Enter the number form 1 to 7: "))
if a == 1:
    print("Its Sunday")
elif a == 2:
    print("Its Monday")
elif a == 3:
    print("Its Tuesday")
elif a == 4:
    print("Its Wednesday")
elif a == 5:
    print("Its Thursday")
elif a == 6:
    print("Its Friday")
elif a == 7:
    print("Its Saturday")
else:
    print("please enter a valid number! ")
