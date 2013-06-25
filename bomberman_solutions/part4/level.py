import pyglet
from square import *

class Level():
  ''' A class that represents a typical level '''
  
  grid = [] # This defines a list
  block_size = 30
  grid_width = 20
  grid_height = 20
  
  
  def __init__(self):
  
    # First thing we do is create a basic looking level of blanks
    for i in range(0,self.grid_height):
      self.grid.append([])  # Create a new empty list
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
    
    column = int(xpos) // 30 # This converts xpos to an integer then divides
    row = ypos // 30
    
    print(column, row) # Print it out, just to make sure!
    
    return self.grid[row][column].allows_movement
    