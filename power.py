# find a^b
a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))
result = 1
for i in range(b):
    result *= a
print(result)
