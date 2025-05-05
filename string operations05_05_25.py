
def reverse_string(s):
    return s[::-1]
def count_characters(s):
    count = {}
    for char in s:
        if char != " ":  
            count[char] = count.get(char, 0) + 1
    return count
def replace_substring(s, old, new):
    return s.replace(old, new)
text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))
char_count = count_characters(text)
print("Character count:")
for char, cnt in char_count.items():
    print(f"'{char}': {cnt}")
old_sub = input("Enter substring to replace: ")
new_sub = input("Enter new substring: ")
print("Modified string:", replace_substring(text, old_sub, new_sub))
