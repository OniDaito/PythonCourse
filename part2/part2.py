''' In this version, we introduce long comments, a way to represent 
the grid using lists of lists and loops and maybe one class '''


import pyglet
import gridsquare

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




grid = []
grid_image = pyglet.resource.image('grid_texture.png')

# a function that creates a nice grid for us
def create_grid():
	for i in range(0,10):
		grid.append([])
		for j in range (0,10):
			grid[i].append(gridsquare.GridSquare(grid_image,False,False,False,False))

# a function that draws a grid
def draw_grid():
	for i in range(0,10):
		for j in range (0,10):
			gridsquare = grid[i][j]
			
			gridsquare.grid_sprite.x = i * 50
			gridsquare.grid_sprite.y = j * 50
			gridsquare.grid_sprite.draw()


# Something that occurs when the A button is pressed
@window.event
def on_key_press(symbol, modifiers):
	print 'A key was pressed'


# When the window is drawn, do stuff
@window.event 
def on_draw():
	window.clear()
	label.draw()
	
	# draw our grid
	draw_grid()
	
	#image.blit(0, 0)

	pacman_sprite.draw()	
	
	
	
# Update our game state
def update(dt): 
	# Move 10 pixels per second 
	pacman_sprite.x += dt * 10
	
# Call Create grid
create_grid()

# Call the update mathod repeatedly 	
pyglet.clock.schedule_interval(update, 1/60.)

# Finally, run the app
pyglet.app.run()