class animal:
    location = "Austrlia"
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speaking now...")
    
class dog(animal):
    def speak(self):
        super().speak()  # Calling the speak method of the parent class
        print("Woof! barks.")
class cat(animal):
    def speak(self):
        super().speak()  # Calling the speak method of the parent class
        print("Meow! meows.")
    
d = dog("Bruno")
d.speak()  # Calling the speak method of the dog class
print(d.location)  # Accessing the class variable location from the dog instance

c = cat("Whiskers")
c.speak()  # Calling the speak method of the cat class  
print(c.location)  # Accessing the class variable location from the cat instance