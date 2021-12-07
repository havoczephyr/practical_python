import random as rand

def random_guess():
    print('why hello there =]')
    name = input('whats your name?')
    print(f'alright then {name}, between 1 and 100, what is the mystery number?')
    random_number = rand.randint(1, 100)
    print (random_number)
    while True:
        guess = int(input('make a guess: '))
        if (guess == random_number):
            print (f'congrats! you got it! the number was {random_number}')
            break
        elif(guess > random_number):
            print (f"you're guess of {guess} too high!")
        elif(guess < random_number):
            print (f"you're guess of {guess} too low!")

random_guess()
