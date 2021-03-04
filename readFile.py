""" 
Joseph Whiteaker 
3/4/2021 
I am copying and pasting chunks of my online textbook and having it read to me because I don't feel like reading it. 
"""

from os import system as terminal


def readOutLoud(fileText):
    terminal("say -v Samantha '{}' ".format(fileText))


openFile = open("putTextHere.txt", "r")

readOutLoud(openFile.read())
