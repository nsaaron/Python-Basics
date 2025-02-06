# Guessing Game
import random 

print( "Welcome to the Guessing Game! I will choose a number between 1 and 10. Guess the Number!")
Random_number = random.randint(1,10)
guess = 0
attempts =  3


while(guess != Random_number):
    if attempts == 0:
        print("Game Over!")
        break
    print("You have %i attempts!"% attempts)
    guess = int(input("Your Guess: "))
    attempts -= 1
    
    if guess == Random_number:
        print("Congradulations! You guessed it!")
        break
    
    if guess > Random_number:
        print("Too High! Try again.")
    
    if guess < Random_number:
        print("Too Low! Try again")
        