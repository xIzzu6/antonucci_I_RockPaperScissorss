# set up a container with our choices inside, and let the AI pick one randomly
from gameComponents import gameVars, chooseWinner, comparison

# create a variable stack - bits of data that can (and will) change

# set up our game loop
while gameVars.player is False:
	# this is the player choice

	if gameVars.player_lives != 0 or gameVars.ai_lives != 0:

		print("================*/ RPS GAME */=================")
		print("Computer Lives:", gameVars.ai_lives, "/", gameVars.total_lives)
		print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
		print("========================================")

		# \n means new line
		print("Choose your weapon! or type quit to exit\n")
		# RPS Game - give the user some weapon options
		gameVars.player = input("Choose rock, paper or scissors: \n")

		# if the player chose to quit, then exit the game
		if gameVars.player == "quit":
			print("you chose to quit")
			exit()

		# check to see what the user input

		# print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
		print("user chose: " + gameVars.player)


		comparison.comparison(gameVars.player)

		if gameVars.player_lives == 0:
			chooseWinner.winorlose("lost")

		elif gameVars.ai_lives == 0:
			chooseWinner.winorlose("won")

		gameVars.player = False
		# computer = choices[randint(0, 2)]

	




	#print("You lose! Would you like to play again?")
		#choice = input("Y / N? ")

		#if choice == "N" or choice == "n":
			#print("You chose to quit! Better luck next time!")
			#exit()

		#elif choice == "Y" or choice == "y":
			# reset the player lives and the AI lives 
			# and set player to False so that our loop will restart
			#player_lives = 1
			#ai_lives = 1
			#player = False

		#else:
			#print("Make a valid choice - Y or N")
			# this will generate a bug that we need to fix later
			#choce = input("Y / N: ")

	

		#if ai_lives is 0:
		#winorlose("won")

		#print("You won! Would you like to play again?")
		#choice = input("Y / N: ")

		#if choice == "N" or choice == "n":
			#print("You chose to quit! Better luck next time!")
			#exit()

		#elif choice == "Y" or choice == "y":
			# reset the player lives and the AI lives 
			# and set player to False so that our loop will restart
			#player_lives = 1
			#ai_lives = 1
			#player = False

		#else:
			#print("Make a valid choice - Y or N")
			# this will generate a bug that we need to fix later
			#choce = input("Y / N")

	# make loop keep running by setting player back to False
	#unset, so that our loop condition above will evaluae to True
	
