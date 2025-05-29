# s = "hello world" #strings are immutable in python
# # s[0] = 'H' # we cannot do this as strings are immutable
# a = len(s)  # length of the string
# print(a) 
# print(s.upper(),s)  # convert to uppercase and original string doesn't changes
# print(s.lower(),s)  # convert to lowercase and original string doesn't changes
# print(s.title()) # convert to title case (first letter of each word capitalized)
# print(s.capitalize())  # capitalizes first character of the string 

# text = "  Hello World  "
# print(text.strip())  # removes leading and trailing whitespace output: "Hello World"
# print(text.lstrip())  # removes leading or left whitespace output: "Hello World  "
# print(text.rstrip())  # removes trailing or right whitespace output: "  Hello World"

# text = "Python is fun"
# print(text.replace("fun", "awesome"))  # replaces 'fun' with 'awesome' output: "Python is awesome"
# print(text.find("fun"))  # finds the index of 'fun' output: 10 

# text = "Apple, Banana, Cherry"
# print(text.split(", "))  # splits the string and converts into a list at each comma and space output: ['Apple', 'Banana', 'Cherry']
# print(", ".join(['Apple', 'Banana', 'Cherry']))  # joins the list into a string with ', ' as separator output: "Apple, Banana, Cherry"

text = "Python12345678"
print(text.isalpha())  # checks if all characters are alphabets output: False
print(text.isdigit())  # checks if all characters are digits  output: False
print(text.isalnum())  # checks if all characters are alphanumeric which contains alphabets and numbers output: True
print(text.isspace())  # checks if all characters are whitespace output: False