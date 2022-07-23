#---------------------------------------------------------------------------------------------------    Password checker - a program that ask's the user for username and password and prints a
#                      message saying how long his password is.
#---------------------------------------------------------------------------------------------------

username = input('What is your username: ')
user_password = input('What is your password: ')
password_length = len(user_password)
hidden_password = '*' * password_length

print(f'{username}, your password {hidden_password} is {password_length} letters long')