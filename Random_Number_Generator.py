import random
secret_number = random.randint(1, 10)

while True:
	guess = int(input("Guess a number between 1 and 10: "))

	if guess == secret_number:
		print("You guessed it! The number was: {}!".format(secret_number))
		break
	elif guess > secret_number:
		print("Sorry, but your guess is to high. Please try again!")
	elif guess < secret_number:
		print("Sorry, but your guess is to low. Please try again!")

