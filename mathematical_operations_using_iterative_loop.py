
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def find_largest(numbers):
    return max(numbers)
def area_of_circle(radius):
    return 3.14 * radius * radius
def area_of_rectangle(length, width):
    return length * width
def area_of_triangle(base, height):
    return 0.5 * base * height
print("Factorial of 5 is:", factorial(5))
nums = [10, 45, 3, 22, 67]
print("Largest number is:", find_largest(nums))
print("Area of circle with radius 5:", area_of_circle(5))
print("Area of rectangle 4x6:", area_of_rectangle(4, 6))
print("Area of triangle (base 3, height 7):", area_of_triangle(3, 7))
