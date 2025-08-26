#print the count of digits of n number.
n = int(input("Enter an integer N: "))
count = 0
digit = n
while digit != 0:
    digit = digit // 10
    count += 1
print(count)
