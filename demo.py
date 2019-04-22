import random

secret_number = random.randint(1, 10)
guess_count = 0
guess_limit = 3

print('Welcome to this little game.')
print('Before starting i need some information about you.')

name = input("Whats's your name? ")

print(f'Ok, {name}, now i need a confirm if you want start this little game.')

y_n = input("You want start this game? (Y for yes, N for no) ")

if y_n.upper() == "Y":
    print("Ok let's start!!!")
    print('Rule: You need guess a number from 1 to 10.')
    while guess_count < guess_limit:
        guess = int(input('Guess Number: '))
        guess_count +=1
        if guess == secret_number:
            print('You Won, really done!')
            break
        else:
            print(f'Sorry, failed, attempts remaining {guess_limit - guess_count} ')
else:
    print('Oh ok, we can do another day.')
