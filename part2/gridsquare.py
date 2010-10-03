''' This class allows the pacman to move in certain directions only '''

import pyglet

# This class is really just a special kind of sprite

class GridSquare():	
	
	def __init__(self, img, allows_move):
		
		# This is a dictionary. Dictionaries allow us to map on value to another
		move_permissions = {}
		
		self.grid_sprite = pyglet.sprite.Sprite(img)
		
		self.move_permissions['left'] = allow_left
		self.move_permissions['right'] = allow_right
		self.move_permissions['up'] = allow_up
		self.move_permissions['down'] = allow_down
			
	