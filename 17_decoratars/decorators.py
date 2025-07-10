#Decorators are functions that takes a function as an argument and returns a new function that adds some kind of functionality to the original function.
def decorators(func):
    def wrapper():
        print("I am about to print hello.....")
        func()
        print("I have excuted the function")
    return wrapper

@decorators
def say_hello():
    print("Hello")

say_hello()

# @decorators
# def say_hello():
#     print("Hello")
# # say_hello() will now automatically have the decorator applied
# # say_hello()

f = decorators(say_hello)
f()

# How f() will look like after applying the decorator:
# def f():
#         print("I am about to print hello.....")
#         print("Hello")
#         print("I have excuted the function")

# Output:
# I am about to print hello.....
# I am about to print hello.....
# Hello
# I have excuted the function
# I have excuted the function
#reasoning:
#When you use @decorators above say_hello, the function say_hello is already decorated.
# Then, you do f = decorators(say_hello). But say_hello is already wrapped, so you are wrapping it again.
# When you call f(), it runs the outer wrapper, which calls the inner wrapper, which then calls the original say_hello.
# Step-by-step:
# Outer wrapper prints: I am about to print hello.....
# Inner wrapper prints: I am about to print hello.....
# Original say_hello prints: Hello
# Inner wrapper prints: I have excuted the function
# Outer wrapper prints: I have excuted the function