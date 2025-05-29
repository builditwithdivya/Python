age = int(input("Enter your age: "))

if (age > 18):
    print("You can drive")
    print("Thank you for your time")

elif (age == 18):
    print("Lets schedule an interview")
    print("Thank you for your time")
    
elif( age == 0):
    print("You are just born")
    print("Thank you for your time")

else:
    print("You cannot drive")
    print("Please wait until you are 18")

print("End of the program")
# The elif statement is used to check multiple conditions.
# If the first condition is false, it checks the next condition.
# If the second condition is also false, it checks the next condition, and so on.
# If all conditions are false, it executes the else block.
# The elif statement is short for "else if".
# You can have multiple elif statements in a single if-else block.