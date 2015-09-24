import random

prior_guesses = [] #use snakecase for python
guess_found = 0
guesses_taken = 0

number = random.randint(1, 100)
username = raw_input("Hi there! What is your name? ")
print "%s I'm thinking of a number from 1-100. Try to guess my number!" % username

while guess_found < 1:
   guess = raw_input('Please take a guess. ')

   if guess.isdigit(): #use this isdigit to make sure the user is entering a number
       guesses_taken = guesses_taken + 1
       guess = int(guess)
       if guess in prior_guesses:
           print("Oopsie, you've already guessed this!")
      
       if guess < number:
           print('Your guess is too low.')
           prior_guesses.append(guess)
      
       elif guess > number:
           print('Your guess is too high.')
           prior_guesses.append(guess)
      
       elif guess == number:
           guesses_taken = str(guesses_taken) #changed guesses_taken into str to concatanate
           print('You are super awesome! You solved this in ' + guesses_taken + ' guesses!')
           guess_found = 1 #this is to break out of the while loop

   else:
       print("That's not a number!")

#use ctrl+h for the replace all function
#python supports boolean values, so we an set while True


