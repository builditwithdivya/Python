#sstring formatting

template = "Dear {} \nYou are {}. \nSo take this ${} bag"
a = "John"
a1 = "awesome"
a2 = 10000
b = "Jack"
b1 = "good"
b2 = 5000
c = "Marie"
c1 = "nice"
c2 = 2000
print(template.format(a, a1, a2))


print(f"{a} is {a1} and he has ${a2} bag")

print(ord("A")) # prints the ASCII value of 'A' output: 65
print(chr(65)) # prints the character for ASCII value 65 output: 'A'