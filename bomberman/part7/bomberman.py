import pyglet
from pyglet.resource import ResourceNotFoundException

class Bomberman():
	
	''' This is a dictionary. It allows assignment of one thing to another '''
	sprites = {}
	currentframe = {}
	current_sprite = None
	
	dimensions = {}
	
	''' This x and y is the bottom left of bomberman '''
	x = 0
	y = 0
	speed = 5

	def __init__(self, startx, starty):
		try:
			left1_img = pyglet.resource.image('images/bomberman_left_1.png')
			left2_img = pyglet.resource.image('images/bomberman_left_2.png')
			left3_img = pyglet.resource.image('images/bomberman_left_3.png')
			
			right1_img = pyglet.resource.image('images/bomberman_right_1.png')
			right2_img = pyglet.resource.image('images/bomberman_right_2.png')
			right3_img = pyglet.resource.image('images/bomberman_right_3.png')
			
			up1_img = pyglet.resource.image('images/bomberman_up_1.png')
			up2_img = pyglet.resource.image('images/bomberman_up_2.png')
			up3_img = pyglet.resource.image('images/bomberman_up_3.png')
			
			down1_img = pyglet.resource.image('images/bomberman_down_1.png')
			down2_img = pyglet.resource.image('images/bomberman_down_2.png')
			down3_img = pyglet.resource.image('images/bomberman_down_3.png')
			
		except (RuntimeError, TypeError, NameError):
			pass
		except ResourceNotFoundException:
			print "You made a typo!"
			exit()
	
		''' Lets put together each frame as a set of tuples. '''
		
		''' FOR YOU - rather than just one x_img lets have 3 together
		as a tuple for left right up and down '''
	
	
	
		# this dictionary keeps a record of which frame we are currently on 
		self.currentframe = {"up": 0, "down" : 0, "left" : 0, "right" : 0}
		
		
		# This line sets which sprite we are drawing from a dictionary and tuple
		self.current_sprite = self.sprites["up"][0]
		
		
		self.current_sprite.x = startx
		self.current_sprite.y = starty
		self.x = startx
		self.y = starty
		
		''' We make another dictionary for the bounding box of bomberman'''
		self.dimensions["width"] =	18
		self.dimensions["height"] = 25
	
	def draw(self) :
		''' Of course, we should update the current sprites x and y '''
		self.current_sprite.x = self.x
		self.current_sprite.y = self.y
		self.current_sprite.draw()
		
	def moveLeft(self):
		self.x -= self.speed
		
		''' FOR YOU - We need to grab the current frame, 
		increment it and then set it back for each move function. Once we
		have the right sprite, we can set the self.current_sprite to the 
		right one'''
		
	
		
	
	def moveRight(self):
		
		
		
	def moveUp(self):
		
	
	def moveDown(self):
		
		