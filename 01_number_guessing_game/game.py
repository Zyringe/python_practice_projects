import random
import math

lower_bound = int(input("Please enter the lower bound of your guess: "))
upper_bound = int(input("Please enter the higher bound of your guess: "))

answer = random.randint(lower_bound, upper_bound)

min_no_guess = math.ceil(math.log(upper_bound - lower_bound + 1, 2))

guess_counter = 0

while min_no_guess > guess_counter:
    guess_counter += 1
    guess = int(input("Please enter your guess: "))
    if guess == answer:
        print("Congratulations!")
        break
    elif guess < answer:
        print("Try Again! You guessed too small")
    elif guess > answer:
        print("Try Again! You guessed too big")
else:
    print(f"The answer is {answer}. Better Luck New Time!")