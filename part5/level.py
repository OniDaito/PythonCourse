''' A class that defines a level - A level is generally 10 x 10 grid squares
with actual grid classes in each space, referencing a certain image '''

from gridsquare import GridSquare as Gs
import pyglet

class Level():

	grid = None
	
	def __init__(self):
			
		# The corners of the maze
		grid_corner_top_left = pyglet.resource.image('images/grid_corner_top_left.png')
		grid_corner_top_right = pyglet.resource.image('images/grid_corner_top_right.png')
		grid_corner_bottom_left = pyglet.resource.image('images/grid_corner_bottom_left.png')
		grid_corner_bottom_right = pyglet.resource.image('images/grid_corner_bottom_right.png')
	
		# The edges of the maze
		
		grid_edge_left = pyglet.resource.image('images/grid_edge_left.png')
		grid_edge_right = pyglet.resource.image('images/grid_edge_right.png')
		grid_edge_top = pyglet.resource.image('images/grid_edge_top.png')
		grid_edge_bottom = pyglet.resource.image('images/grid_edge_bottom.png')

		grid_blank = pyglet.resource.image('images/grid_blank.png')
	
		tl = Gs(grid_corner_top_left,False,True,False,True)
		print tl
		te = Gs(grid_edge_top,False,True,True,True)
		tr = Gs(grid_corner_top_right,False,True,True,False)
		
		le = Gs(grid_edge_left,True,True,False,True)
		re = Gs(grid_edge_right,True,True,True,False)
		
		bl = Gs(grid_corner_bottom_left, True, False, False, True)
		br = Gs(grid_corner_bottom_right, True, False, True, False)
		be = Gs(grid_edge_bottom, True, False, True, True)
		
		a = Gs(grid_blank,True,True,True,True)
		
		print a
		
		# Laying out a grid like this alters our up downness remember
	
		self.grid = [
			[tl,te,te,te,te,te,te,te,te,tr], 
			[le,a,a,a,a,a,a,a,a,re],
			[le,a,a,a,a,a,a,a,a,re],
			[le,a,a,a,a,a,a,a,a,re],
			[le,a,a,a,a,a,a,a,a,re],
			[le,a,a,a,a,a,a,a,a,re],
			[le,a,a,a,a,a,a,a,a,re],
			[le,a,a,a,a,a,a,a,a,re],
			[le,a,a,a,a,a,a,a,a,re],
			[bl,be,be,be,be,be,be,be,be,br]
		]
		
	def returnGridSquare(self, x,y):
		return self.grid [ ((500 - y) / 50) - 1] [ x / 50]
	

	def draw(self):
		for i in range(0,10):
			for j in range (0,10):
				gridsquare = self.grid[i][j]
			
				gridsquare.grid_sprite.y = 450  - (i * 50)
				gridsquare.grid_sprite.x = j * 50
				gridsquare.grid_sprite.draw()