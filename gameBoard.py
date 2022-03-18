import pygame
import time

# set up color var constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



class Game_Board:
	def __init__(self, surface):
		self.surface = surface

		self.surface.fill(WHITE)

		# creates list of Board Buttons
		self.buttons = []

		# button positions that are winning positions 
		# button positions start at top left pos 0 and end at bottom right pos 8
		self.winning_Positions = [[0, 3, 6], [1, 4, 7], [2, 5, 8],
							[0, 1, 2], [3, 4, 5], [6, 7, 8],
							[0, 4, 8], [2, 4, 6]]

		# creates list of x
		self.xs = []

		# creates list of o
		self.os = []

		# creates a font
		self.font = pygame.font.Font('freesansbold.ttf', 32)

		# if the game has finished
		self.game_Over = False

		# creates the game board
		self.create_Board()

	'''
	Creates white buttons for the players to click on to add their shapes.
	Then draws the lines to create the boundaries for the buttons.
	'''
	def create_Board(self):
		# position = 0
		pos = 0

		# creates the invisible buttons for the tic tac toe board
		y = 100
		for i in range(3):
			x = 100
			for i in range(3):
				self.buttons.append(Board_Button(pygame.Rect(x, y, 200, 200), self.surface, pos))
				x += 200
				pos += 1
			y += 200

		# creates the lines that make the tic tac toe board
		pygame.draw.line(self.surface, BLACK, (300, 100), (300, 700), 8)
		pygame.draw.line(self.surface, BLACK, (500, 100), (500, 700), 8)
		pygame.draw.line(self.surface, BLACK, (100, 300), (700, 300), 8)
		pygame.draw.line(self.surface, BLACK, (100, 500), (700, 500), 8)


	'''
	Goes through all the winning Poisitions then checks the lists of xs and os clicked
	by the players, and checks if any of the winning Pos combos are in the lists of
	xs and os. If they are then a winning Line is drawn to indicate the winner as 
	long with a message displaying the winner.
	'''
	def check_Winner(self):
		for i in range(len(self.winning_Positions)):
			# the first button pos in winning Positions
			first_Pos = self.winning_Positions[i][0]

			# the second button pos in winning Positions
			second_Pos = self.winning_Positions[i][1]

			# the third button pos in winning Positions
			third_Pos = self.winning_Positions[i][2]

			# if the first, second, and third button pos are all in the list button pos
			# clicked by player 1
			if first_Pos in self.xs and second_Pos in self.xs and third_Pos in self.xs:
				self.draw_Winning_Line(i, first_Pos, third_Pos, BLUE)
				self.display_Winner(1, BLUE)
				self.game_Over = True

			# if the first, second, and third button pos are all in the list button pos
			# clicked by player 2
			if first_Pos in self.os and second_Pos in self.os and third_Pos in self.os:
				self.draw_Winning_Line(i, first_Pos, third_Pos, RED)
				self.display_Winner(2, RED)
				self.game_Over = True


	'''
	Displays which player won at the top of the screen. 
	'''
	def display_Winner(self, player, color):
		winning_Text = self.font.render(f"Player {player} has won!", True, color)
		winning_Rect = winning_Text.get_rect()
		winning_Rect.center = (400, 50)
		self.surface.blit(winning_Text, winning_Rect)

	def display_Draw(self):
		draw_Text = self.font.render("The game has ended in a draw!", True, (128, 0, 128))
		draw_Rect = draw_Text.get_rect()
		draw_Rect.center = (400, 50)
		self.surface.blit(draw_Text, draw_Rect)


	'''
	Displays a button to ask the user to play again at the bottom of the screen.
	'''
	def prompt_Restart(self):
		restart_Text = self.font.render("Play again?", True, BLACK)
		self.restart_Rect = restart_Text.get_rect()
		self.restart_Rect.center = (400, 800)
		self.surface.blit(restart_Text, self.restart_Rect)

	'''
	Draws a winning Line through the winning combo.
	Finds the first button based on the start Pos and the 
	last button based on the last Pos. The winning Positions
	are arranged with the first three being vertical wins,
	the next three are horizontal wins, the last two are diagnol
	wins.
	'''
	def draw_Winning_Line(self, button_Pos, start_Pos, last_Pos, color):
		for i in range(len(self.buttons)):
			# finds the first Button in the winning combo
			if i == start_Pos:
				first_Button = self.buttons[i]

			# finds the last Button in the winning combo
			if i == last_Pos:
				last_Button = self.buttons[i]

		# the winning combo is a verticle win
		if 0 <= button_Pos and button_Pos <= 2:
			pygame.draw.line(self.surface, color, first_Button.rectangle.midtop, last_Button.rectangle.midbottom, 8)
		
		# the winning combo is a horizontal win
		elif 3 <= button_Pos and button_Pos <= 5:
			pygame.draw.line(self.surface, color, (first_Button.rectangle.midleft), (last_Button.rectangle.midright),  8)
		
		# the winning combo is a diagnol win from top left to bottom right
		elif button_Pos == 6:
			pygame.draw.line(self.surface, color, (first_Button.rectangle.topleft), (last_Button.rectangle.bottomright), 8)
		
		# the winning combo is a diagnol win from bottom left to top right
		else:
			pygame.draw.line(self.surface, color, (first_Button.rectangle.topright), (last_Button.rectangle.bottomleft), 8)
		




class Board_Button:
	def __init__(self, rectangle, surface, position):
		# allows us to access the buttons rectangle properties
		self.rectangle = rectangle
		self.surface = surface
		self.position = position
		self.clicked = False
		self.shape = ""

	'''
	Adds a shape to the board based on the player, only if the button has not
	been clicked on already then appends the buttons position to the list
	depending on the player.
	'''
	def add_Shape(self, shape, shape_List):
		if shape == "O" and not self.clicked:
			pygame.draw.circle(self.surface, RED, (self.rectangle.center), 50, 6)
			self.clicked = True
			self.shape = shape
			

		if shape == "X" and not self.clicked:
			top = self.rectangle.top 
			left = self.rectangle.left 
			bottom = self.rectangle.bottom 
			right = self.rectangle.right 
			
			pygame.draw.line(self.surface, BLUE, (left + 50 , top + 50), (right - 50, bottom - 50), 6)
			pygame.draw.line(self.surface, BLUE, (left + 50, bottom - 50), (right - 50, top + 50), 6)
			
			self.clicked = True
			self.shape = shape

		# appends to the list of either xs or os
		shape_List.append(self.position)



class Player:
	def __init__(self, shape):
		self.shape = shape
		self.winner = False
		self.loser = False

