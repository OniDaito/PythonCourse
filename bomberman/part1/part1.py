import pyglet

''' A simple version of bomberman. Each tile is 30x30 so we can 
make a grid with various blocks that bomber can/can't move
through or destroy/not destroy. We use the Pyglet Library 
as it runs easily on most platforms. '''


# Create a Window 600 x 600 gives a 20 x 20 grid size
window = pyglet.window.Window(600,600) 


# Load an image from the disk
bomberman_image = pyglet.resource.image('images/bomberman_down_1.png')

# Create one sprite from this
bomberman_sprite = pyglet.sprite.Sprite(bomberman_image)


# Something that occurs when the A button is pressed
@window.event
def on_key_press(symbol, modifiers):
	print 'A key was pressed'


# When the window is drawn, do stuff
@window.event 
def on_draw():
	window.clear()
	bomberman_sprite.draw()	
	
# Update our game state
def update(dt): 
	''' FOR YOU: Try to get the bomberman sprite to move every time 
	update is called. dt is a number (delta time) and sprite has a member
	variable called x and another called y'''
	
	pass
	
	
# Call the update mathod repeatedly 	
pyglet.clock.schedule_interval(update, 1/60.)

# Finally, run the app
pyglet.app.run()