''' This class allows the pacman to move in certain directions only '''

import pyglet

class Pacman():

	# We can do this as part of initialisation, unlike other langauges
	# Load an image from the disk
	pacman_image = pyglet.resource.image('images/pacman.png')

	# Create one sprite from this
	pacman_sprite = pyglet.sprite.Sprite(pacman_image)

	# underscores are often used in Python to denote variables
	# and methods that are often internal to the class and
	# shouldnt really be called by th outside world directly
	_x = 0;
	_y = 0;

	def __init__(self):
		# Anchor the pacman to his centre	
		self.pacman_sprite.anchor_x = self.pacman_sprite.width / 2 
		self.pacman_sprite.anchor_y = self.pacman_sprite.height / 2
	
	
	def moveRight(self):
		self._x += 10
		
	def moveLeft(self):
		self._x -= 10
		
	def moveUp(self):
		self._y += 10
		
	def moveDown(self):
		self._y -= 10
	
	def draw(self):
		self.pacman_sprite.x = self._x
		self.pacman_sprite.y = self._y
		
		self.pacman_sprite.draw()