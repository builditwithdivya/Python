a = 45

b = 58

# Arithmetic Operators
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction  
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division 
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a ** b)  # Exponentiation

# Comparison Operators
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to
print("a > b:", a > b)    # Greater than
print("a < b:", a < b)    # Less than
print("a >= b:", a >= b)  # Greater than or equal to
print("a <= b:", a <= b)  # Less than or equal to

# Assignment Operators
a += b  # Add and assign
print("a after a += b:", a)
a -= b  # Subtract and assign
print("a after a -= b:", a)
a *= b  # Multiply and assign       
print("a after a *= b:", a)
a /= b  # Divide and assign
print("a after a /= b:", a)
a //= b  # Floor divide and assign
print("a after a //= b:", a)
a %= b  # Modulus and assign
print("a after a %= b:", a)
a **= b  # Exponentiate and assign
print("a after a **= b:", a)

# Logical Operators
print("a > b and a < 100:", a > b and a < 100)  # Logical AND
print("a > b or a < 100:", a > b or a < 100)    # Logical OR    
print("not (a > b):", not (a > b))  # Logical NOT

# Identity Operators
print("a is b:", a is b)  # Identity is
print("a is not b:", a is not b)  # Identity is not

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print("3 in my_list:", 3 in my_list)  # Membership in
print("6 not in my_list:", 6 not in my_list)  # Membership not in

# Ternary Operator
result = "a is greater than b" if a > b else "a is not greater than b"
print("Ternary Operator Result:", result)  # Ternary operator