
n = int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
