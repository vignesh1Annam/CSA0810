n = int(input("Enter a number: "))

print("Ascending order:")
for i in range(1, n + 1):
    print(i, end=' ')

print("\nDescending order:")
for i in range(n, 0, -1):
    print(i, end=' ')
