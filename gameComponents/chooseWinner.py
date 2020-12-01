from gameComponents import gameVars

# define a win or lose function
def winorlose(status):
	# print("called winorlose", satus)

	if status == "won":
		pre_message = "You are the winner! Congrats! "

	else:
		pre_message = "You lost:( "

	print(pre_message + " Would you like to play again?")

	choice = input("Y / N?")

	if choice == "Y" or choice == "y":
		
		# reset the game and start over again
		gameVars.player_lives = 5
		gameVars.ai_lives = 5
		gameVars.player = False

	elif choice == "N" or choice == "n":
		# exit message and quit
		print("You chose to quit. Better luck next time!")
		exit()

	else:
		print("Make a valid choice - Y or N")
		# this is generating a bug -> need to fix this check
		choice = input("Y / N?")
