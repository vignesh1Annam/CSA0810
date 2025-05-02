n = int(input("Enter a number: "))
sum_squares = sum(i * i for i in range(1, n + 1))
print(f"Sum of squares of first {n} natural numbers is {sum_squares}")
