import pyglet
from pyglet.resource import ResourceNotFoundException

class Bomberman():
  
  ''' This is a dictionary. It allows assignment of one thing to another '''
  sprites = {}
  current_sprite = None
  
  dimensions = {}
  
  ''' This x and y is the bottom left of bomberman '''
  x = 0
  y = 0
  speed = 5

  def __init__(self, startx, starty):
    
    ''' FOR YOU : There is a chance we might screw this up so we should surround
    it with some exceptions '''
    
    
    left_img = pyglet.resource.image('images/bomberman_lef_1.png')
    right_img = pyglet.resource.image('images/bomberman_right_1.png')
    up_img = pyglet.resource.image('images/bomberman_up_1.png')
    down_img = pyglet.resource.image('images/bomberman_down_1.png')
    
    self.sprites["left"] = pyglet.sprite.Sprite(left_img)
    self.sprites["right"] = pyglet.sprite.Sprite(right_img)
    self.sprites["up"] = pyglet.sprite.Sprite(up_img)
    self.sprites["down"] = pyglet.sprite.Sprite(down_img)
    
    self.current_sprite = self.sprites["up"]
    self.current_sprite.x = startx
    self.current_sprite.y = starty
    self.x = startx
    self.y = starty
    
    ''' We make another dictionary for the bounding box of bomberman'''
    self.dimensions["width"] =  18
    self.dimensions["height"] = 25
  
  def draw(self) :
    ''' Of course, we should update the current sprites x and y '''
    self.current_sprite.x = self.x
    self.current_sprite.y = self.y
    self.current_sprite.draw()
    
  def moveLeft(self):
    ''' FOR YOU - update the move methods so Bomberman does things '''
  
  def moveRight(self):
    
    
  def moveUp(self):
    
  
  def moveDown(self):
    
    