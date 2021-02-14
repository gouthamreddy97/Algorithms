from random import *

print('1: rock \n2: paper\n3: scissors')

def rps_game():
	inp = int(input('Please enter a number:'))
	game = ['rock', 'paper', 'scissors']
	if 1<=inp<=3: 
		if inp == 1:
			print(f'you have selected {game[0]}')
		elif inp == 2:
			print(f'you have selected {game[1]}')
		elif inp == 3:
			print(f'you have selected {game[2]}')
		shuffle(game)
		game = game[0]
		print(f'system selected {game}')

		if (inp==1 and game=='rock') or (inp==2 and game=='paper') or (inp==3 and game=='scissors'):
			print('DRAW')
		else:
			if inp == 1 and game =='scissors' :
				print('YOU WON')
			elif inp == 2 and game =='rock':
				print('YOU WON')
			elif inp == 3 and game =='paper':
				print('YOU WON')
			else:
				print('YOU LOST')
	else:
		print('Please select a number from 1,2,3')
while True:
	rps_game()