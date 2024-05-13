import random
import string
adjectives = ['green', 'tall', 'ugly', 'buffalo', 'violent', 'Orange', 'short', 'pink', 'yellow', 'purple', 'adoravle', 'adventurous', 'aggressive', 'average', 'alert']
nouns = ['Man', 'Buffalo', 'McDonalds', 'WendysFourForFour', 'WendysFiveDollarBiggie', 'Table', 'Bottle', 'Child', 'Brother', 'Monkey', 'Lion', 'Girl', 'Boy', 'City', 'Beach',]
#numbers = [1,2,3,4,5]
#special_characters = ['$', '@', '&', '#', '?']
number_of_passwords = None
print('Welcome to the Python Password Picker!/n')
number_of_passwords = int(input('Please enter the number of passwords you would like.'))
while True:
    for num in range(number_of_passwords):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        #number = random.choice(numbers)
        number = random.randrange(0, 1000)
        #special_character = random.choice(special_characters)
        special_character = random.choice(string.punctuation)
       

        password = adjective + noun + str(number) + special_character
        print('This is your secure password: %s' % password)

    response = input("Would you like to choose another password? type y or n: ").lower()
    if response == 'n':
        break
    elif response == "":
        break
    number_of_passwords = int(input('Please enter the number of passwords you would like: '))
