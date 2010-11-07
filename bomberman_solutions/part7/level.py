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
							ø
			xpos = 0
			ypos = self.grid_height -1 
			
			for line in f:
				''' Each line is a row in our grid but remember that with 
				lists and arrays, 0,0 is the top left whereas in our actual
				game, 0,0 is the bottom left'''
				
				self.grid.append([])
				newrow = self.grid[len(self.grid) -1]
			
				for block in line:
					realx = xpos * self.block_size
					realy = ypos * self.block_size
				
					if block == "_":
						newrow.append(BlankSquare(realx,realy))
						
					elif block == "E":
						newrow.append(EdgeSquare(realx,realy))
						
					elif block == "B":
						newrow.append(BrickSquare(realx,realy))
					
					elif block == "S":
						newrow.append(StoneSquare(realx,realy))
						
					xpos += 1
					
				xpos = 0
				ypos -= 1
				
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
		
		column = int(xpos) / 30 # This converts xpos to an integer then divides
		row = ypos // 30 # this does a float division then *floors* the result
		
		print column, row # Print it out, just to make sure!
		
		return self.grid[row][column].allows_movement
		