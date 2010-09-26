''' In this version, we introduce long comments, a way to represent 
the grid using lists of lists and loops and maybe one class '''


import pyglet
import gridsquare
import pacman
from pyglet.window import key

# Create a Window
window = pyglet.window.Window(500,600)


# Make some labels for the scores 
label = pyglet.text.Label('Score', font_name='Times New Roman',
				font_size=36, 
				x=10, 
				y=window.height - 20, 
				anchor_x='left', 
				anchor_y='center')


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


# create our pacman

pacman_player = pacman.Pacman()


# Something that occurs when the A button is pressed
@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.LEFT:
		pacman_player.moveLeft()	
	elif symbol == key.RIGHT:
		pacman_player.moveRight()
	elif symbol == key.UP:
		pacman_player.moveUp()
	elif symbol == key.DOWN:
		pacman_player.moveDown()

# When the window is drawn, do stuff
@window.event 
def on_draw():
	window.clear()
	label.draw()
	
	# draw our grid
	draw_grid()
	pacman_player.draw()
	
	
# Update our game state
def update(dt): 
	pass
	
# Call Create grid
create_grid()

# Call the update mathod repeatedly 	
pyglet.clock.schedule_interval(update, 1/60.)

# Finally, run the app
pyglet.app.run()