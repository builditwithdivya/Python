def sum(a,b):
    global z  # Declare 'z' as a global variable and please modify it
    c = a + b
    z = 7  # This modifies the global variable 'z'
    return c

z = 16  # Global variable
# The variable 'z' is defined in the global scope, so it can be accessed inside the function 'sum'
print(sum(4, 6))  # Output: 10
print(z)  # Output: 7, because 'z' was modified inside the function
# The variable 'z' is now modified to 7 inside the function 'sum', so it reflects the change globally