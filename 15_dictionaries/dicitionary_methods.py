marks = {"John": 85, "Alice": 90, "Bob": 78}  # Dictionary of student marks

marks.values()  # Returns a view object that displays a list of all the values in the dictionary
marks.keys()  # Returns a view object that displays a list of all the keys in the dictionary
marks.items()  # Returns a view object that displays a list of key-value tuple pairs in the dictionary
print(marks.get("Alice"))  # Returns the value for the specified key, or None if the key does not exist
print(marks.pop("John"))  # Removes the specified key and returns its value
