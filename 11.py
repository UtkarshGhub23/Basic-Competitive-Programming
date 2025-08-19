# 11. Take a number A as input, print its multiplication table having the first 10 multiples.
# Input:-3



A = int(input("Enter an integer A: "))
for i in range(1, 11):
    print(f"{A} * {i} = {A*i}")
