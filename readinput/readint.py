# source https://realpython.com/python-input-integer/
number_as_string = input("Please enter an integer: ")
#Please enter an integer: 123
print(f"The value of the string is {number_as_string}")

#number_as_integer = int(number_as_string)
#print(f"The value of the integer is {number_as_integer}")
number_as_integer = None
while number_as_integer is None:
    try:
        number_as_integer = int(input("Please enter an integer: "))
    except ValueError:
        print("Invalid integer!")
        print(f"The integer you entered was {number_as_integer}")