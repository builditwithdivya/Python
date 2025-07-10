class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sum(self, other):
        return point(self.x + other.x, self.y + other.y)
    def print_point(self):
        print(f"Point({self.x}, {self.y})")
    def __add__(self, other):
        # This method is called when the + operator is used
        return point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        # This method is called when the - operator is used
        return point(self.x - other.x, self.y - other.y)

p1 = point(2, 3)
p2 = point(5, 7)

# p = p1.sum(p2)  # Using the sum method to add two points
# p.print_point()  # Printing the result of the sum
p = p1 + p2 # This will raise an error because the + operator is not overloaded
# To use the + operator, we need to overload it in the point class 
p.print_point()  # Printing the first point
p3 = p2 - p1  # This will raise an error because the - operator is not overloaded
# To use the - operator, we need to overload it in the point class
p3.print_point()  # Printing the result of the subtraction