''' A file with a set of functions designed to handle the game logic '''

import level
import gridsquare

# can pacman move in this direction in this grid square?
def canMove(direction, pacman, current_level):
		
	square = current_level.returnGridSquare(pacman._x,pacman._y)

	
	return square.move_permissions[direction]