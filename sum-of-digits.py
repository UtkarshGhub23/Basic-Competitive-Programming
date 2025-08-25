# 9
# take input
N = int(input("Enter an integer N: "))
sum_digits = 0
temp = N
# using while loop
while temp != 0:
    digit = temp % 10
    sum_digits += digit
    temp = temp // 10
print(sum_digits)
