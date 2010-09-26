import pyglet

# Create a Window
window = pyglet.window.Window(500,600)


# Make some labels for the scores 
label = pyglet.text.Label('Score', font_name='Times New Roman',
				font_size=36, 
				x=10, 
				y=window.height - 20, 
				anchor_x='left', 
				anchor_y='center')

# Load an image from the disk
pacman_image = pyglet.resource.image('pacman.png')

# Create one sprite from this
pacman_sprite = pyglet.sprite.Sprite(pacman_image)

# Anchor the pacman to his centre	
pacman_sprite.anchor_x = pacman_sprite.width / 2 
pacman_sprite.anchor_y = pacman_sprite.height / 2

# Something that occurs when the A button is pressed
@window.event
def on_key_press(symbol, modifiers):
	print 'A key was pressed'


# When the window is drawn, do stuff
@window.event 
def on_draw():
	window.clear()
	label.draw()
	#image.blit(0, 0)

	pacman_sprite.draw()	
	
# Update our game state
def update(dt): 
	# Move 10 pixels per second 
	pacman_sprite.x += dt * 10
	
	
# Call the update mathod repeatedly 	
pyglet.clock.schedule_interval(update, 1/60.)

# Finally, run the app
pyglet.app.run()