''' A file with a set of functions designed to handle the game logic '''


# Where in our grid is pacman?
def getPacmanGridSquare(pacman):
	px = pacman._x
	py = pacman._y
	
	return (px / 50, py / 50)
	
# can pacman move in this direction in this grid square?
def canMove(direction, gridsquare):
	return gridsquare.move_permissions[direction]