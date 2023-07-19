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

# look for which functions are implemented in each module by using the dir function:
>>> import urllib
>>> dir(urllib)
['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener', '__all__', '__builtins__', 
'__doc__', '__file__', '__name__', '__package__', '__version__', '_ftperrors', '_get_proxies', 
'_get_proxy_settings', '_have_ssl', '_hexdig', '_hextochr', '_hostprog', '_is_unicode', '_localhost', 
'_noheaders', '_nportprog', '_passwdprog', '_portprog', '_queryprog', '_safe_map', '_safe_quoters', 
'_tagprog', '_thishost', '_typeprog', '_urlopener', '_userprog', '_valueprog', 'addbase', 'addclosehook', 
'addinfo', 'addinfourl', 'always_safe', 'basejoin', 'c', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 
'getproxies_environment', 'getproxies_macosx_sysconf', 'i', 'localhost', 'main', 'noheaders', 'os', 
'pathname2url', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_macosx_sysconf', 'quote', 
'quote_plus', 'reporthook', 'socket', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 
'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'test', 'test1', 
'thishost', 'time', 'toBytes', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname', 'urlcleanup', 'urlencode', 
'urlopen', 'urlretrieve']

#  we can read more about it with the help function, using the Python interpreter:
help(urllib.urlopen)

# Writing packages
# Packages are namespaces containing multiple packages and modules. They're just directories, but with certain requirements.
# Each package in Python is a directory which MUST contain a special file called __init__.py. This file, which can be empty, indicates that the directory it's in is a Python package. That way it can be imported the same way as a module.
# If we create a directory called foo, which marks the package name, we can then create a module inside that package called bar. Then we add the __init__.py file inside the foo directory.
# To use the module bar, we can import it in two ways:

import foo.bar
from foo import bar

# The __init__.py file can also decide which modules the package exports as the API, while keeping other modules internal, by overriding the __all__ variable like so:
__init__.py:

__all__ = ["bar"]