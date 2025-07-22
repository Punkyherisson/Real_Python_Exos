#Chapter 4: Strings
#Strings are sequences of characters enclosed in quotes.
phrase="Hello World"
apostrophe = "It's a beautiful day"
multiline_string = """This is a multiline string.
It can span multiple lines."""
long_string = "This multiline string is \
 displayed on one line"
print(long_string)
print(multiline_string)
print(type(phrase))
longueur=len(phrase)
final_index = len(longueur)- 1
print(longueur)
#print(phrase[longueur]) # This will raise an IndexError because the index is out of range
print(phrase[final_index])  # last character using calculated index

print(phrase[-1])  # last character
letter1 = phrase[0]
print(letter1)
last_letter = phrase[-1]
print(phrase[0:5])

print("Spock said, \"Live long and prosper.\"")
vulcan_logic="Spock said, \"Live long and prosper.\""
vulcan_logic = 'Spock said, "Live long and prosper."'
topping1 = "Peanut Butter"
topping2 = "Jelly"
sandwich=topping1 +" & "+topping2  
print(sandwich)
