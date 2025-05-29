a = int(input("Enter a lucky number between 1 and 10: "))

match a:
    
    case 1:
        print("You won a car!")
    case 3:
        print("You won a bike!")
    case 5:
        print("You won $3000!")
    case 7:
        print("You won a trip to Hawaii!")
    case _:
        print("Better luck next time")
# The match-case statement is used to match a value against multiple patterns.
# It is similar to the switch-case statement in other programming languages.