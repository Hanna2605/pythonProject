# Write a code to return "Hero" from given string
example_string1 = "Hello bro"

# Write a code to return "Jack is my name"
example_string2 = "jack Is My NAME"

# Write a code to return "Get rid of stars please"
example_string3 = "*Get rid of stars please*"

# Write a code to return "Hello my name is Jack"
example_string4 = "hello my name is jack"

# Write a code to return formatted string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"

# Write a code to return byte_string text value
byte_string = b"\316\273"

# Write a code to return True if cost is greater than 500$
example_string5 = "It cost me 1000.00$"

print(example_string1[0:2] + example_string1[7:9])

print(example_string2.capitalize())

print(example_string3.strip('*'))

print(example_string4[0].upper() + example_string4[1:17] + example_string4[17].upper() + example_string4[18:])

print(var2.capitalize() + ',' + var3.lower() + ' ' + var1.capitalize())

print(byte_string.decode('utf-16'))

cost = float((example_string5[11:]).strip('$'))
if cost > float(500):
    print(True)
else:
    print(False)



