def repeat(n):
    def decorator(func):
        def wrapper(a):
            for _ in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(3)

def say_hello(name):
    print(f"Hello, {name}!")
    
say_hello("Divya")


# Input looks like this:
# for _ in range(n):
#     say_hello("Divya")
# Output:
# Hello, Divya!
# Hello, Divya!   
# Hello, Divya!
