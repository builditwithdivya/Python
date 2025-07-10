class Employee:
    def __init__(self, name, salary, bond):
        self.name = name
        self.salary = salary
        self.bond = bond
    
    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"Name: {self.name}\n Salary: {self.salary}\n Bond: {self.bond} years")
    
e1 = Employee("Alice", 50000, 2)  # Creating an instance of the Employee class with name, salary, and bond
print(e1.get_salary())  # Calling the get_salary method to get the salary of the employee
e1.get_info()  # Calling the get_info method to display the employee's information
