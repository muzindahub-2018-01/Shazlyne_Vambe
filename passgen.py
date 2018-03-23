#password generator@python!

#To select random characters import random library
import random

#Create a list of characters stored in a variable called chars.
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"%&()_+:@~?|/#'

#Ask user to input password length stored in variable length
length = input('Password length? ')

#Convert user's input into a whole number
length = int(length)

#To create 5 passwords
for p in range(5):

    #To choose a random character from the list create a variable called password
    password = ''

    #You want to repeat as many times as the user entered
    for c in range(length):
        password += random.choice(chars)
    print(password)


