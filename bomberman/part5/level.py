import pyglet
from square import *

class Level():
	''' A class that represents a typical level '''
	
	grid = [] # This defines a list
	block_size = 30
	grid_width = 20
	grid_height = 20
	
	
	def __init__(self, level_file):
		''' We modify out init method to allow a file to be passed in. 
		If this value is nil then we can just generate a basic level but if
		not, lets try to load the proper thing '''
		
		if level_file:
			f = open(level_file, 'r') # can be w,r, r+ or a
			
			current_row = self.grid_height
			
			xpos = 0
			ypos = self.grid_height - 1
			
			for line in f:
				''' Each line is a row in our grid but remember that with 
				lists and arrays, 0,0 is the top left whereas in our actual
				game, 0,0 is the bottom left'''
				
				
				''' FOR YOU - for each line, append a new list to the grid
					then read each character on the line and append a different
					kind of block to each row depending on what we have read.
					
					Each time, we need to increment the real position as well '''
				
				
				
			# Add in a reverse to get the level the right way
			# But remember, we need to adjust the ypos too!
			self.grid.reverse()
	
		else:		
			for i in range(0,self.grid_height):
				self.grid.append([])	# Create a new empty list
				for j in range(0,self.grid_width):
					self.grid[i].append(
					BlankSquare(j * self.block_size, i * self.block_size))
					
				
		
	def draw(self):
		''' Draw out the level by looping through each grid square and calling
		the draw function'''
		
		for row in self.grid:
			for block in row:
				block.draw()
				

	
	def canMoveHere(self, xpos, ypos):
		''' Given an xpos and ypos within the screen, find the block at that
		point and return true if bomberman can move into it or false if he
		cant. 
		
		We need to convert x and y into block indexes with a little maths.'''
		
		column = xpos // 30 
		row = ypos // 30 # this does a float division then *floors* the result
		
		print(column, row) # Print it out, just to make sure!
		
		return self.grid[row][column].allows_movement
		