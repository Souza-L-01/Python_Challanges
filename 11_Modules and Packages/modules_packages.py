# Writing modules
# Modules in Python are just Python files with a .py extension. The name of the module is the same as the file name. A Python module can have a set of functions, classes, or variables defined and implemented. 

# game.py
# import the draw module
import draw

def play_game():
	...

def main():
	result = play_game()
	draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
	main()


# The draw module may look something like this:
# draw.py
def draw_game():
	...

def clear_screen(screen):
	...

# Importing all objects from a module
# use the import * command to import all the objects in a module

# game.py
# import the draw module
from draw import *

def main():
    result = play_game()
    draw_game(result)