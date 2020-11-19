# set up a container with our choices inside, and let the AI pick one randomly
from random import randint

# an array is a datatype in nerd talk => arrays are 0-based
# every entry gets an index
choices = ["rock", "paper", "scissors"]

# computer is our AI opponent - let it make choice
computer = choices[randint(0, 2)]

# give our player and our AI some lives
player_lives = 5
ai_lives = 5

# True and False are boolean data types -> the equivalent of 1 and 0
player = False

while player is False:

	# RPS Game - give the user some weapon options
	player = input("Pick rock, paper or scissors: ")

	#player = True 

	# validate that the input worked
	print("Player chose " + player)
	print("AI chose: " + computer)

	# check to see who won or if it's a tie
	if (computer == player):
		print("tie")
		# reset the game loop and have the user choose again

	elif (computer == "rock"):
		if (player == "scissors"):
			print("you lose!")
			# take a life away from the player
			player_lives = player_lives - 1
		else:
			print("you won!")
			# take a life away from the AI
			ai_lives = ai_lives - 1

	elif (computer == "paper"):
		if (player == "rock"):
			print("you lose!")
			# take a life away from the player
			player_lives = player_lives - 1
		else:
			print("you won!")
			# take a life away from the AI
			ai_lives = ai_lives - 1

	elif (computer == "scissors"):
		if (player == "paper"):
			print("you lose!")
			# take a life away from the player
			player_lives = player_lives - 1
		else:
			print("you won!")
			# take a life away from the AI
			ai_lives = ai_lives - 1

	print("Player has", player_lives, "lives left")
	print("AI has", ai_lives, "lives left")

	# make loop keep running by setting player back to False
	#unset, so that our loop condition above will evaluae to True
	player = False
