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

#-----------------------------------------------------------
#     String concatenation - adding strings together
#-----------------------------------------------------------
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

#-----------------------------------------------------------
#                   Formatted strings
#-----------------------------------------------------------
name = 'Luis'
age = 17

# f string
print(f'Hi {name}. You are {age} years old')    # For python 3 and newer versions.

print('Hi {}. You are {} years old'.format(name, age))   # For older python versions.
print('Hi {1}. You are {0} years old'.format(name, age))    # Can change the order by indexing them.
print('Hi {new_name}.'.format(new_name = 'Jesus'))      # Can also create new variable to use.

#-----------------------------------------------------------
#            String Slicing/String Indexing
#-----------------------------------------------------------
pet_name = 'Sombra'
print(pet_name[0])    # string_name[index] - returns value of string at the given index
print(pet_name[0:3])    # [start_index:end_index] - returns value from start to end index
print(pet_name[0:5:1])  # [start:end:step] - returns value from start to end with given step value
print(pet_name[0:5:2])
print(pet_name[0:])     # If no end index is given, then goes until the end.
print(pet_name[:3])     # If no start is given, then starts at the beginning.
print(pet_name[::1])    # Can also just modify step value only.

# Negative Index
print(pet_name[-1])     # Negative implies starting from the end.
print(pet_name[::-1])   # Usefule for reversing a string.

# Immutability
# You can't change a single part of the string only. MUST CHANGE ENTIRE STRING!
