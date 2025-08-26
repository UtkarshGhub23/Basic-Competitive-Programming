#find and return the sum of even numbers between 1 to n
a = int(input("Enter an integer a: "))
sum = 0
for i in range(2, a+1, 2):
    sum += i
print(sum)
