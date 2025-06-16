tu = (23, 45, 67, 89, 90, 45, 78, 90) 

print(tu.count(45))  # Count occurrences of 45 in the tuple
print(tu.index(90))  # Find the index of the first occurrence of 90

'''Why to use tuples?
Faster than lists: Tuples are generally faster than lists for iteration and access due to their immutability.
Used as dictionary keys: Tuples can be used as keys in dictionaries, while lists cannot.
Safe from accidental modification: Since tuples are immutable, they cannot be changed after creation, making them safer for data that should not be modified.
'''