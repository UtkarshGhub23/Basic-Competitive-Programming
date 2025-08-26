#print the sum of all odd numbers between 1 to n
a = int(input("Enter an integer a: "))
sum = 0
for i in range(1, a+1, 2):
    sum += i
print(sum)
