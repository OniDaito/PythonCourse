import pyglet

class GridSquare():
	''' This text is special as it forms the description
	of the class that is automagically read out with the __doc__
	command '''
		
	allows_movement = False
	xpos = 0
	ypos = 0
	
	# This is the constructor. This takes an xpos and ypos of the
	# grid and whether or not bomberman can move into this spot
	
	def __init__(self, xpos, ypos, allows_movement):
		self.allows_movement = allows_movement
		self.xpos = xpos
		self.ypos = ypos
		
	
	def draw(self):
		self.sprite.x = xpos * 30
		self.sprite.y = ypos * 30
		self.sprite.draw()
			
	
	
class EdgeSquare(GridSquare):
	''' A Square that sits at the edge, usually made of metal 
	We dont need to define class variables all the time. We can
	just add them to self whenever we feel like it, more or less '''
	
	def __init__(self,xpos,ypos):
		GridSquare.__init__(self,xpos,ypos,False)
		self.img = pyglet.resource.image('images/edge_block.png')
		self.sprite = pyglet.sprite.Sprite(self.img)
		
		#	This is the python 2.7+ way of doing super classes
		#	super(GridSquare, self).__init__(xpos,ypos,false)


class BlankSquare(GridSquare):
	''' An empty space that allows movement'''
	def __init__(self,xpos,ypos):
		GridSquare.__init__(self,xpos,ypos,True)
		self.img = pyglet.resource.image('images/blank_block.png')
		self.sprite = pyglet.sprite.Sprite(self.img)


class StoneSquare(GridSquare):
	''' A Square that doesnt allow movement and appears like stone'''
	def __init__(self,xpos,ypos):
		GridSquare.__init__(self,xpos,ypos,False)
		self.img = pyglet.resource.image('images/stone_block.png')
		self.sprite = pyglet.sprite.Sprite(self.img)


class BrickSquare(GridSquare):
	''' A Square that can be destroyed by a bomb '''
	def __init__(self,xpos,ypos):
		GridSquare.__init__(self,xpos,ypos,False)
		self.img = pyglet.resource.image('images/brick_block.png')
		self.sprite = pyglet.sprite.Sprite(self.img)