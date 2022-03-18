import pygame, sys
from gameBoard import *


def main():
	pygame.init()
	game = pygame.display
	WIDTH = 800
	HEIGHT = 900
	DISPLAYSURF = game.set_mode((WIDTH, HEIGHT))
	game.set_caption("Tic-Tac-Toe")

	board = Game_Board(DISPLAYSURF)
	player_1 = Player("X")
	player_2 = Player("O")

	turn = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			# checks if a player has won the game
			board.check_Winner()

			if board.game_Over:
				# prompts players to restart game with button
				board.prompt_Restart()

				# if player clicks restart button
				if board.restart_Rect.collidepoint(mouse_Position):
					main()

			# if the game ends in a draw
			if turn == 9 and not board.game_Over:
				board.game_Over = True
				board.display_Draw()


			# displays an x if it is player 1s turn and the game is not over
			if turn % 2 == 0 and not board.game_Over:
				pygame.draw.line(DISPLAYSURF, BLUE, (725, 825), (775, 875), 6)
				pygame.draw.line(DISPLAYSURF, BLUE, (775, 825), (725, 875), 6)
			
			# displays a circle if it is player 2s turn and the game is not over
			if turn % 2 == 1 and not board.game_Over:
				pygame.draw.circle(DISPLAYSURF, RED, (50, 850), 25, 6)

			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_Position = event.pos

				# loops through all the board buttons
				for i in board.buttons:

					# if a player hit within a box that has not been clicked
					if i.rectangle.collidepoint(mouse_Position) and not i.clicked \
						and not board.game_Over:

						# clears the previous players turn
						pygame.draw.rect(DISPLAYSURF, WHITE, (0, 800, 800, 100))

						# if it is player 1s turn
						if turn % 2 == 0:
							# adds the x to screen
							i.add_Shape(player_1.shape, board.xs)

						# if it is player 2s turn
						else:
							# adds the circle to screen 
							i.add_Shape(player_2.shape, board.os)

						# only changes the turn when a box is hit
						turn += 1
	
		pygame.display.update()
				
		

if (__name__ == "__main__"):
	main()