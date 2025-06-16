#Create a list containing the table of 5 

a = 5
table = []

for i in range(1, 11):
    table.append(a * i)

print(table)
# List comprehension to create the table of 5
table_comprehension = [a * i for i in range(1, 11)]
print(table_comprehension)

#List comprehension to create a list of squares of even numbers from 0 to 20
squares_of_evens = [i ** 2 for i in range(21) if i % 2 == 0]
print(squares_of_evens)