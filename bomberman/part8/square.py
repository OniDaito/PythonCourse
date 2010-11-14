import pyglet

class GridSquare():
  ''' This text is special as it forms the description
  of the class that is automagically read out with the __doc__
  command '''
    
  allows_movement = False

  
  # This is the constructor. This takes an xpos and ypos of the
  # grid and whether or not bomberman can move into this spot
  
  def __init__(self, allows_movement):
    self.allows_movement = allows_movement
    
  
  def draw(self):
    self.sprite.draw()
  
class EdgeSquare(GridSquare):
  ''' A Square that sits at the edge, usually made of metal 
  We dont need to define class variables all the time. We can
  just add them to self whenever we feel like it, more or less '''
  
  def __init__(self, xpos, ypos):
    GridSquare.__init__(self,False)
    self.img = pyglet.resource.image('images/edge_block.png')
    self.sprite = pyglet.sprite.Sprite(self.img)
    self.sprite.x = xpos
    self.sprite.y = ypos
    
    # This is the python 2.7+ way of doing super classes
    # super(GridSquare, self).__init__(xpos,ypos,false)


class BlankSquare(GridSquare):
  ''' An empty space that allows movement'''
  def __init__(self, xpos, ypos):
    GridSquare.__init__(self,True)
    self.img = pyglet.resource.image('images/blank_block.png')
    self.sprite = pyglet.sprite.Sprite(self.img)
    self.sprite.x = xpos
    self.sprite.y = ypos


class StoneSquare(GridSquare):
  ''' A Square that doesnt allow movement and appears like stone'''
  def __init__(self, xpos, ypos):
    GridSquare.__init__(self,False)
    self.img = pyglet.resource.image('images/stone_block.png')
    self.sprite = pyglet.sprite.Sprite(self.img)
    self.sprite.x = xpos
    self.sprite.y = ypos


class BrickSquare(GridSquare):
  ''' A Square that can be destroyed by a bomb '''
  def __init__(self, xpos, ypos):
    GridSquare.__init__(self,False)
    self.img = pyglet.resource.image('images/brick_block.png')
    self.sprite = pyglet.sprite.Sprite(self.img)
    self.sprite.x = xpos
    self.sprite.y = ypos
    

''' This is *almost* like decorating but we are actually replacing.
What this function does is replace the function inside the square
with another allowing runtime replacement. Decorating runs another 
function before *returning* the other function. '''

''' FOR YOU - finish the add a bomb function. Ive begun it for you.
The idea is to get the subfunction "bombDraw" to call the EXISTING 
function for drawing then draw the bobm sprite. Dont forget to set
the square's draw function to the new one we just made '''
      
def addBomb(square) :
  f = square.draw
  img = pyglet.resource.image('images/bomb_1.png')
  sprite = pyglet.sprite.Sprite(img)
  
  def bombDraw():
    pass
  
  
''' FOR YOU - Finish off the addAnimatedBomb. This uses a generator
and the yield statement '''
  
def addAnimatedBomb(square) :

  f = square.draw
  img1 = pyglet.resource.image('images/bomb_1.png')
  sprite1 = pyglet.sprite.Sprite(img1)
  img2 = pyglet.resource.image('images/bomb_2.png')
  sprite2 = pyglet.sprite.Sprite(img2)
  img3 = pyglet.resource.image('images/bomb_3.png')
  sprite3 = pyglet.sprite.Sprite(img3)
  
  def bombDrawAnim():
    sprites = [sprite1,sprite2,sprite3]
    pos = 0
    while 1:
      ''' what we need to do here is call f(), loop
      pos and then YIELD the correct drawing function '''
      pass
    
  anim = bombDrawAnim()
  
  square.draw = anim.next

  
