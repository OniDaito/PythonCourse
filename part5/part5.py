''' In this version, we introduce long comments, a way to represent 
the grid using lists of lists and loops and maybe one class '''


import pyglet
import gridsquare
import pacman
import gamelogic
import level

from pyglet.window import key

# Create a Window
window = pyglet.window.Window(500,600)

# This allows us to constantly check if a button is held down
keys = key.KeyStateHandler() 
window.push_handlers(keys)

# Make some labels for the scores 
label = pyglet.text.Label('Score', font_name='Times New Roman',
				font_size=36, 
				x=10, 
				y=window.height - 20, 
				anchor_x='left', 
				anchor_y='center')



# create our pacman
pacman_player = pacman.Pacman()

# create our first level
current_level = level.Level()


# When the window is drawn, do stuff
@window.event 
def on_draw():
	window.clear()
	label.draw()
	current_level.draw()	

	pacman_player.draw()
	
	
# Update our game state
def update(dt): 
	

	if keys[key.LEFT] and gamelogic.canMove( 'left', pacman_player, current_level ):
		pacman_player.moveLeft()
		
	if keys[key.RIGHT] and gamelogic.canMove( 'right',  pacman_player, current_level ):
		pacman_player.moveRight()
	
	if keys[key.UP] and gamelogic.canMove( 'up',  pacman_player, current_level ):
		pacman_player.moveUp()
		
	if keys[key.DOWN] and gamelogic.canMove( 'down',  pacman_player, current_level ):
		pacman_player.moveDown()
	
	

# Call the update mathod repeatedly 	
pyglet.clock.schedule_interval(update, 1/60.)

# Finally, run the app
pyglet.app.run()