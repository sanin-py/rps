# Colors
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'










# Introduction to the game.
print(f'''
  {color.BOLD}{color.UNDERLINE}Play{color.END}{color.UNDERLINE} {color.CYAN}Rock Paper Scissors{color.END}{color.UNDERLINE} {color.BOLD}with computer{color.END}

• You will be playing with a computer program made by me.
• By default, there are 3 rounds in the game.\n  But, if you want to change the number of rounds, you can do that as well.
• One with the most number of {color.GREEN}points{color.END} at the end of\n  the final round will win.
• If you feel like, to stop the game in between, just enter 'Quit'.
• Choose Rock, Paper, or Scissors; type what you chose and click Enter.
• Computer will choose from the same and send along with you :)
''')










# Enter START to begin the game.
while True:
	begin = input(f'''• Type {color.YELLOW}Start{color.END} below and click Enter to begin:
~ ''').lower()
	if begin == 'start':
		break
	else:
		print('  I can\'t understand you.')










# User can choose howmany rounds he/she wants.
print("• Do you want to change the number of rounds?")
while True:
	change_rounds = input(f"  Enter {color.YELLOW}Y{color.END} (yes) to change and {color.YELLOW}N{color.END} (no) to not.\n~ ").lower()
	if change_rounds == 'y':
		while True:
			try:
				rounds_user_needs = input("• Howmany rounds do you need?\n~ ")
				if rounds_user_needs == '0':
					print("  Is it possible to play a game with zero rounds you idiot?")
					continue
				rounds_user_needs = int(rounds_user_needs)
				break
			except ValueError:
				print("  You are supposed to enter only a counting number (as number, not word).")
				continue
		break
	elif change_rounds == 'n':
		rounds_user_needs = 3
		break
	else:
		continue

if rounds_user_needs == 1:
	print(f"  Alright, {rounds_user_needs} round set.")

else:
	if rounds_user_needs > 20:
		print(f"  {rounds_user_needs} rounds! That's hell of a selection. Let's see who wins.\n  {rounds_user_needs} rounds set.")
	else:
		print(f"  Alright, {rounds_user_needs} rounds set.")










# The rules of Stone, Paper and Scissors are coded from here on.
import random
computer_options = ['Rock','Paper','Scissors']
rounds = 0
computer_points = 0
user_points = 0
while rounds < rounds_user_needs:
	print()
	print('• Round ' + f'{rounds + 1}')
	user_choice = input(f'''  Choose Rock, Paper, or Scissors.
  {color.GREEN}You:{color.END} ''').title()
	computer_choice = random.choice(computer_options)
	print(f'  {color.RED}Computer:{color.END} ' + computer_choice)


	if user_choice == computer_choice:
		enter = input('  Click Enter to continue ')
		while enter != '':
			enter = input('  Click Enter to continue ')
		else:
			print(f"  Since both you and computer have entered {user_choice}, {color.BLUE}it's a  draw{color.END}.")
			rounds += 1


	elif user_choice == 'Scissors' and computer_choice == 'Rock':
		enter = input('  Click Enter to continue ')
		while enter != '':
			enter = input('  Click Enter to continue ')
		else:
			print(f"  Rock smashes Scissors. {color.RED}So computer scored +1 point{color.END}.")
			rounds += 1
			computer_points += 1


	elif user_choice == 'Rock' and computer_choice == 'Scissors':
		enter = input('  Click Enter to continue ')
		while enter != '':
			enter = input('  Click Enter to continue ')
		else:
			print(f"  Rock smashes Scissors. {color.GREEN}So you scored +1 point{color.END}.")
			rounds += 1
			user_points += 1


	elif user_choice == 'Paper' and computer_choice == 'Scissors':
		enter = input('  Click Enter to continue ')
		while enter != '':
			enter = input('  Click Enter to continue ')
		else:
			print(f"  Scissors cut  paper. {color.RED}So computer scored +1 point{color.END}.")
			rounds += 1
			computer_points += 1


	elif user_choice == 'Scissors' and computer_choice == 'Paper':
		enter = input('  Click Enter to continue ')
		while enter != '':
			enter = input('  Click Enter to continue ')
		else:
			print(f"  Scissors cut  paper. {color.GREEN}So you scored +1 point{color.END}.")
			rounds += 1
			user_points += 1


	elif user_choice == 'Rock' and computer_choice == 'Paper':
		enter = input('  Click Enter to continue ')
		while enter != '':
			enter = input('  Click Enter to continue ')
		else:
			print(f"  Paper covers rock. {color.RED}So computer scored +1 point{color.END}.")
			rounds += 1
			computer_points += 1


	elif user_choice == 'Paper' and computer_choice == 'Rock':
		enter = input('  Click Enter to continue ')
		while enter != '':
			enter = input('  Click Enter to continue ')
		else:
			print(f"  Paper covers rock. {color.GREEN}So you scored +1 point{color.END}.")
			rounds += 1
			user_points += 1


	elif user_choice == '':
		print(f"          {color.RED}:{color.END} Type something man. ")


	elif user_choice == 'Quit':
		print("  Game terminated.")
		rounds_user_needs = 0


	else:
		print(f"          {color.RED}:{color.END} Don't type bullshit man.")










# Game results:
else:
	print()
	print(f"  {color.PURPLE}ALL ROUNDS ARE OVER{color.END}")
	print()
	results = input(f"• Type {color.BOLD}{color.YELLOW}R{color.END} and click Enter to see the final results: ").lower()
	print()
	while results != 'r':
		results = input(f"• Enter {color.BOLD}{color.YELLOW}R{color.END} to see the final results: ").lower()
		print()
	if results == 'r':
		if computer_points == 0:
			print(f'> Computer scored nothing.')

		elif computer_points == 1:
			print(f'> Computer scored a total of {computer_points} point.')

		else:
			print(f'> Computer scored a total of {computer_points} points.')


		if user_points == 0:
			print(f'> You scored nothing.')

		elif user_points == 1:
			print(f'> You scored a total of {user_points} point.')

		else:
			print(f'> You scored a total of {user_points} points.')


		if user_points > computer_points:
			print("> So, you won! 🔰👑🔰")
		elif user_points < computer_points:
			print("> So, you lost!")
		elif user_points == computer_points:
			print("> So, it's a tie!")











# End Credits:
print("")
print('  [A game by Sanin]')
print("")
