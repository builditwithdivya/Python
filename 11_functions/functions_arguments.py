def add(a, b): # a and b are positional arguments
    x = a + b
    return x


c = add(3, 5)
print(c)

def add(a, b, plus=0): #plus is a keyword argument with a default value of 0 so this is called a default argument
    x = a + b + plus
    return x


c = add(3, 5, 2)
print(c)

c1 = add(b=5, a=3)  # b and a are keyword arguments