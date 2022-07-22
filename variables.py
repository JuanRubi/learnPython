#---------------------------------------------------------------------------------------------------                               Variables
#---------------------------------------------------------------------------------------------------

# Variable name best practices
# start with lowercase or underscore
# use underscore as space for readability ex: snake_case
# keep names concise and descriptive
user_name = 'Juan'
print(user_name)
user_age = 26
print(user_age)

# Constants
# use all capital letters for name
PI = 3.14   # Constants have values that won't change

# Augmented assignment operator
# +=, -=, *=
value = 5
value += 5
print(value)

#---------------------------------------------------------------------------------------------------                               Strings
#---------------------------------------------------------------------------------------------------
# Can use double or single quotes for strings.
print(type("Hi there!"))

username = 'user'
password = 'password'

# multi-line strings 
long_string = '''
wow
o o
----
'''
print(long_string)

# String concatenation - adding strings together
first_name = 'Juan'
last_name = 'Rosales'
full_name = first_name + ' ' + last_name
print(full_name)

# Type conversion
num_to_string = str(10)  # integer 10 is converted to a string

# Escape Sequence - backslash quote(s) to tell it quote(s) is a string
weather = "It\'s \"kind of\" sunny"
# \t - tab
# \n - new line