def sum(a, b):
    c = a + b
    z = 7 # This variable 'z' is defined inside the function scope, so it is not accessible outside of it.
    # It creates a local variable 'z' that shadows the global variable 'z'.
    #which gets destroyed after the function returns.
    return c

z = 16  # Global variable
# The variable 'z' is defined in the global scope, so it can be accessed inside the function 'sum'
print(sum(4,6))  # Output: 10
# print(a)
# This will raise an error because 'a' is not defined outside the function scope
# The variable 'a' is defined inside the function 'sum', so it is not accessible outside of it.     
# print(c)
# This will also raise an error because 'c' is not  defined outside the function scope
# The variable 'c' is defined inside the function 'sum', so it is not accessible outside of it.     
print(z)