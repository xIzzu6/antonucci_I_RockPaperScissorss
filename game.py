# set up a container with our choices inside, and let the AI pick one randomly
from random import randint

# an array is a datatype in nerd talk => arrays are 0-based
# every entry gets an index
choices = ["rock", "paper", "scissors"]

# computer is our AI opponent - let it make choice
computer = choices[randint(0, 2)]


# RPS Game - give the user some weapon options
player = input("Pick rock, paper or scissors: ")

# validate that the input worked
print("Player chose " + player)
print("AI chose: " + computer)

# check to see who won or if it's a tie
if (computer == player):
	print("tie")
	# reset the game loop and have the user choose again

elif (computer == "rock"):
	if (player == "scissors"):
		pring("you lose!")
		# take a life away from the player
	else:
		print("you won!")
		# take a life away from the player 

elif (computer == "paper"):
	if (player == "rock"):
		pring("you lose!")
		# take a life away from the player
	else:
		print("you won!")
		# take a life away from the player 

elif (computer == "scissors"):
	if (player == "paper"):
		pring("you lose!")
		# take a life away from the player
	else:
		print("you won!")
		# take a life away from the player 
