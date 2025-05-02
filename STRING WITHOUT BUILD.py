text = input("Enter a string: ")
reversed_str = ''
for char in text:
    reversed_str = char + reversed_str
print(f"Reversed string: {reversed_str}")
