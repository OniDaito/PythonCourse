import pyglet

''' A simple version of bomberman. Each tile is 30x30 so we can 
make a grid with various blocks that bomber can/can't move
through or destroy/not destroy. We use the Pyglet Library 
as it runs easily on most platforms. '''

from level import Level as lvl

from pyglet.window import key

# Create a Window 600 x 600 gives a 20 x 20 grid size
window = pyglet.window.Window(600,600) 

# This allows us to constantly check if a button is held down
keys = key.KeyStateHandler() 
window.push_handlers(keys)


# Load an image from the disk
bomberman_image = pyglet.resource.image('images/bomberman_down_1.png')

# Create one sprite from this
bomberman_sprite = pyglet.sprite.Sprite(bomberman_image)

level1 = lvl()

# When the window is drawn, do stuff
@window.event 
def on_draw():
  window.clear()    
  level1.draw()
  bomberman_sprite.draw() 
  
# Update our game state
def update(dt): 
  
  if keys[key.LEFT]:
    if level1.canMoveHere(bomberman_sprite.x - 5, bomberman_sprite.y):
      bomberman_sprite.x -= 5
    
  if keys[key.RIGHT]:
    if level1.canMoveHere(bomberman_sprite.x + 5, bomberman_sprite.y):
      bomberman_sprite.x += 5
  
  if keys[key.UP]:
    if level1.canMoveHere(bomberman_sprite.x, bomberman_sprite.y + 5):
      bomberman_sprite.y += 5
    
  if keys[key.DOWN]:
    if level1.canMoveHere(bomberman_sprite.x, bomberman_sprite.y - 5):
      bomberman_sprite.y -= 5
  
  
# Call the update mathod repeatedly   
pyglet.clock.schedule_interval(update, 1/60.)

# Finally, run the app
pyglet.app.run()