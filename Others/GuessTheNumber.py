import random

x = random.randint(1, 100)


def myfunc(n):
    return abs(n - x)


guesses = []

print("The Random number is between 1 - 100")

for i in range(3):
    while True:
        try:
            guess = int(input(f"Attempt {i+1}) Guess the number: "))
            if 1 <= guess <= 100:
                break
            else:
                print("The range is from 1 to 100 inclusive. Try again.")
        except ValueError:
            print("Please input only integers.")
    guesses.append(guess)
    if guess == x:
        print(f"You got it in {i+1} attempt! Lucky.")
        break
else:
    guesses.sort(key=myfunc)
    print(f"Unfortunately, you didn't guess: {x} \nYour closest guess was {guesses[0]}")
