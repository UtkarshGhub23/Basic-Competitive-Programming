#Take a number A as input, print its multiplication table having the first 10 multiples.
a = int(input("Enter an integer a: "))
for i in range(1, 11):
    print(f"{a} * {i} = {a*i}")
