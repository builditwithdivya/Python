#Class is a blueprint or template for creating objects.For example, Form for an exam that contains fields like name, age, electives, father's name, mother's name, etc.
## An object is an instance created from a class. For example, if you create a form for a student named John, that form is an object of the class Form.

class Employee:
    company = "TechCorp"  # Class variable shared by all instances of the class
    def get_salary(self):#self is a reference to the current instance of the class
        return 50000 
    
e1 = Employee()  # Creating an instance of the Employee class
print(e1.get_salary())  # Calling the get_salary method on the e1 instance

e2 = Employee()  # Creating another instance of the Employee class
print(e2.get_salary())  # Calling the get_salary method on the e2 instance
# The get_salary method returns the salary of the employee, which is 50000 for both instances
# Each instance of the Employee class can have its own attributes and methods, but in this case, both instances share the same get_salary method.
print(e2.company)#  # Accessing the class variable company from the e2 instance
print(e1.company)  # Accessing the class variable company from the e1 instance 