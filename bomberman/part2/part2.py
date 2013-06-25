import pyglet

pyglet.resource.path=['images']
pyglet.resource.reindex()

''' A simple version of bomberman. Each tile is 30x30 so we can 
make a grid with various blocks that bomber can/can't move
through or destroy/not destroy. We use the Pyglet Library 
as it runs easily on most platforms. '''

import square

# Create a Window 600 x 600 gives a 20 x 20 grid size
window = pyglet.window.Window(600,600) 


# Load an image from the disk
bomberman_image = pyglet.resource.image('bomberman_down_1.png')

# Create one sprite from this
bomberman_sprite = pyglet.sprite.Sprite(bomberman_image)

es = square.EdgeSquare(20,20)

# Something that occurs when the A button is pressed
@window.event
def on_key_press(symbol, modifiers):
  print ('A key was pressed')


# When the window is drawn, do stuff
@window.event 
def on_draw():
  window.clear()
  bomberman_sprite.draw() 
  es.draw()
  
# Update our game state
def update(dt): 
  # Move 10 pixels per second 
  bomberman_sprite.x += dt * 10
  
  
# Call the update mathod repeatedly   
pyglet.clock.schedule_interval(update, 1/60.)

# Finally, run the app
pyglet.app.run()