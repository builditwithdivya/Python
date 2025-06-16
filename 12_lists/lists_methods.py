marks = [54, 32, 67, 89, 23, 45, 78, 90] 
extra_marks = [100, 95, 85]  # List of extra marks
# Adding elements to the list

marks.append(100)  # Adding an element to the end of the list
print(marks)

marks.pop()  # Removing the last element
print(marks)

marks.insert(2, 75)  # Inserting an element at index 2
print(marks)

marks.extend(extra_marks)  # Extending the list with another list
print(marks)

marks.sort()  # Sorting the list in ascending order
print(marks)

marks.reverse()  # Reversing the list
print(marks)

marks.remove(32)  # Removing the first occurrence of 32
print(marks)