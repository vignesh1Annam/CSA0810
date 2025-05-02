def is_perfect(number):
    sum_divisors = sum(i for i in range(1, number) if number % i == 0)
    return sum_divisors == number

num = int(input("Enter a number: "))
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
