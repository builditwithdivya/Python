class Employee:
    company = "TechCorp"  # Class variable shared by all instances of the class
    def __init__(self, name, salary, bond, company):
        self.name = name
        self.salary = salary
        self.bond = bond
        self.company = company
    
    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"Name: {self.name}\n Salary: {self.salary}\n Bond: {self.bond} years")
    
e1 = Employee("Alice", 50000, 2, "Tesla")  # Creating an instance of the Employee class with name, salary, and bond
print(e1.company)  # will always print instance attribute
print(Employee.company)  # will always print class attribute

#object introspection
print(dir(e1))  # Displaying the instance attributes of e1