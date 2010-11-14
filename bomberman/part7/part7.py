import pyglet
import sys

''' A simple version of bomberman. Each tile is 30x30 so we can 
make a grid with various blocks that bomber can/can't move
through or destroy/not destroy. We use the Pyglet Library 
as it runs easily on most platforms. '''

from level import Level as lvl
from pyglet.window import key
from bomberman import Bomberman

''' FOR YOU - surround this with the proper declaration if name equals main '''

# Create a Window 600 x 600 gives a 20 x 20 grid size
window = pyglet.window.Window(600,600) 

level1 = None

''' FOR YOU - assume the user is passing in a path to our level file
Check the sys.argv length and if its equal to 2, set our level file 
to sys.argv[1] '''



# When the window is drawn, do stuff
@window.event 
def on_draw():
  window.clear()    
  level1.draw()
  bm.draw() 

# Update our game state
def update(dt): 
  
  ''' We need to modify our collision detection as bomberman
  has a width and height; he's not just a point! '''
  
  if keys[key.LEFT]:
    if level1.canMoveHere(bm.x  - bm.speed, bm.y):
      bm.moveLeft()
    
  if keys[key.RIGHT]:
    if level1.canMoveHere(bm.x + bm.dimensions["width"] + 5, bm.y):
      bm.moveRight()
  
  if keys[key.UP]:
    if level1.canMoveHere(bm.x, bm.y + bm.dimensions["height"] + 5):
      bm.moveUp()
    
  if keys[key.DOWN]:
    if level1.canMoveHere(bm.x, bm.y - 5):
      bm.moveDown()
  

# This allows us to constantly check if a button is held down
keys = key.KeyStateHandler() 
window.push_handlers(keys)
# load bomberman

bm = Bomberman(31,31)

# Call the update mathod repeatedly   
pyglet.clock.schedule_interval(update, 1/60.)

# Finally, run the app
pyglet.app.run()