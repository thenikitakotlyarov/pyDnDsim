#!/usr/bin/env python3
#^                   ^
# \_________________/
#  |
#this first line declares that this is running in python3



##this is how to import modules in python
#import os
##writing it as below imports everything in the root
##of the named module, in this case the `__init__.py` file

from __init__ import *

import sys

class Pyglet_Skeleton:
    def __init__(self , params):
        self.name = params.get('name')
        self.age = params.get('age')
        self.occupation = params.get('occupation')

def game():
    game_window = Window(cwidth=screen_width,
                        cheight=screen_height,
                        caption='pyglet_skeleton_test')

    pyglet.app.run()



def main(*args, **kwargs):
    print("running game")
    game()
    print("closing game")
    exit()


if __name__ == '__main__':
    main(sys.argv)


