from gameComponents import gameVars, chooseWinner, comparison
from random import randint

def comparison(status):

# this will be the AI choice -> a random pick from the choices array
	computer = gameVars.choices[randint(0, 2)]

	# validate that the random choice worked for the AI
	print("AI chose: " + computer)

# check to see who won or if it's a tie
	if (computer == gameVars.player):
		print("tie")
		# reset the game loop and have the user choose again

	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			# take a life away from the player
			gameVars.player_lives -= 1
			print("you lose! player lives: ", gameVars.player_lives)
			
		else:
			print("you won!")
			# take a life away from the AI
			gameVars.ai_lives -= 1

	elif (computer == "paper"):
		if (gameVars.player == "rock"):
			# take a life away from the player
			gameVars.player_lives -= 1
			print("you lose! player lives: ", gameVars.player_lives)
			
		else:
			print("you won!")
			# take a life away from the AI
			gameVars.ai_lives -= 1

	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			print("you lose!")
			# take a life away from the player
			gameVars.player_lives -= 1 
		else:
			print("you won!")
			# take a life away from the AI
			gameVars.ai_lives -= 1
