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

# Custom import name
# Modules may be loaded under any name you want. This is useful when importing a module conditionally to use the same name in the rest of the code.
# For example, if you have two draw modules with slighty different names, you may do the following:

# game.py
# import the draw module
if visual_mode:
	# in visual mode, we draw using graphics
	import draw_visual as draw
else:
	# in textual mode, we print out text
	import draw_textual as draw

def main():
	result = play_game()
	# this can either be visual or textual depending on visual_mode
	draw.draw_game(result)

# Module initialization
# The first time a module is loaded into a running Python script, it is initialized by executing the code in the module once. If another module in your code imports the same module again, it will not be loaded again, so local variables inside the module act as a "singleton," meaning they are initialized only once.
# draw.py

def draw_game():
	# when clearing the screen we can use the main screen object initialized in this module
	clear_screen(main_screen)
	...

def clear_screen(screen):
	...

class Screen():
	...

# initialize main_screen as a singleton
main_screen = Screen()

# Extending module load path
PYTHONPATH=/foo python game.py
sys.path.append("/foo")

# built-in modules
# import the library
import urllib
# use it
urllib.urlopen(...)