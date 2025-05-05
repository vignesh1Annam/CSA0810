def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
def area_of_shape(shape, *dimensions):
    if shape == "circle":
        radius = dimensions[0]
        return 3.1416 * radius * radius
    elif shape == "rectangle":
        length, width = dimensions
        return length * width
    elif shape == "triangle":
        base, height = dimensions
        return 0.5 * base * height
    else:
        return "Unknown shape"
num = 5
print(f"Factorial of {num} is {factorial(num)}")
numbers = [10, 45, 3, 22, 67]
print(f"Largest number is {find_largest(numbers)}")
print(f"Area of circle (radius 5): {area_of_shape('circle', 5)}")
print(f"Area of rectangle (4x6): {area_of_shape('rectangle', 4, 6)}")
print(f"Area of triangle (base 3, height 7): {area_of_shape('triangle', 3, 7)}")
