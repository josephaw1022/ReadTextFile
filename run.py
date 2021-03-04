""" 
Joseph Whiteaker 
3/4/2021 
I am copying and pasting chunks of my online textbook and having it read to me because I don't feel like reading it. 
"""

from os import system as terminal


def clear():
    terminal("clear")


try:
    terminal("black *.py")
except:
    print("Warning: The code couldn't be formatted\nCode will still work")
finally:
    print("\n\nCode is running now\n\n{}\n".format("Press ctrl+c to stop reading"))
    terminal("python3 readFile.py")
