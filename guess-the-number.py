import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 to {x} : "))
        if guess < random_number:
            print("Sorry guess again, You enter too low")
        elif guess > random_number:
            print("Sorry guess again, You enter too high")
    print(f'Congrats you guessed the number {random_number}')

# guess(10)



# let computer guess your secret number

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too High(H), too low(L) or correct (C) : ".lower())
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess +1
    print(f'Yay computer guessed the number {guess} correctly ')


# computer_guess(10000)
