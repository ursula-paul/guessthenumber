import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess !=random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        print(guess)
        if guess < random_number:
            print ('sorry,guess again . Too low.')
        elif guess>random_number:
            print ('sorry,guess again. Too high')
            
    print(f'yes, congrats. you guessed the right number {random_number} correctly')   
        
guess(10)