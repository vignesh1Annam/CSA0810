
a = 5
b = 10
print("Before swapping (with temp): a =", a, ", b =", b)
temp = a
a = b
b = temp
print("After swapping (with temp): a =", a, ", b =", b)
x = 15
y = 20
print("\nBefore swapping (without temp): x =", x, ", y =", y)
x, y = y, x 
print("After swapping (without temp): x =", x, ", y =", y)
