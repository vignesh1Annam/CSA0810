num = int(input("Enter a number: "))
total = 0
n = num

while n > 0:
    digit = n % 10
    total += digit
    n = n // 10

print("Sum of digits:", total)
