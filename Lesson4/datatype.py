import math


# String data type

#Literal assignment
first = "Dave"
last = "Stone"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))


# construction function
pizza = str("Pepricorn")
print(type(pizza) == str)
print(isinstance(pizza, str))


# Concatination
fullname = first + " " + last
print(fullname)
fullname += "!"
print(fullname)

# Casting a number to string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like music from " + decade + "s."
print(statement)

#Multiple lines
multiline = '''
Hey, how are you?

I was just checking in

            All good?.
'''
print(multiline)

#Escaping special character
sentence = 'I\'m back at work!\tHey\n\nWhere\'s this at\\located?'
print(sentence)

# string method
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                        "
multiline = "                       " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))


# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffe".ljust(15, ".") + "$1".rjust(4))
print("Muffin".ljust(15, ".") + "$4.22".rjust(4))
print("Chease Cake".ljust(15, ".") + "$12.34".rjust(4))

print(" ")
print(first)
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# some method returns boolean method
print(first.startswith('D'))
print(first.endswith("E"))

#Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(x, bool))


#Integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))


# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(type(y))

# Complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.imag)
print(comp_value.real)

# Build in function for numbers
print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))



print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))