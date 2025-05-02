number = input("Enter a number: ")
digit_sum = 0
for digit in number:
    if digit.isdigit(): 
        digit_sum += int(digit)
print("Sum of digits:", digit_sum)
