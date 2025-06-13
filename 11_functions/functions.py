a = 2
b = 4
c = 9

average = (a + b + c) / 3
print(average)

a1 = 25
b1 = 43
c1 = 12

average1 = (a1 + b1 + c1) / 3
print(average1)

def average_of_three(a, b, c):
    d = (a + b + c) / 3
    print(d)

o1 = average_of_three(2, 4, 9)
o2 = average_of_three(4, 7, 12)

print(o1)# None is printed because the function does not return a value
print(o2)# None is printed because the function does not return a value

def average_of_three_return(a, b, c):
    d = (a + b + c) / 3
    return d

r1 = average_of_three_return(2, 4, 9)
r2 = average_of_three_return(4, 7, 12)
print(r1)  # This will print the average of 2, 4, and 9 
print(r2)  # This will print the average of 4, 7, and 12