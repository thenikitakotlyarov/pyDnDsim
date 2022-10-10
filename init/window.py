#!/usr/bin/env python3

import pyglet
from pyglet import window as pw

class Window(pw.Window):
    def __init__(self,cwidth, cheight, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.win_size = cwidth, cheight
        self.main_batch = pyglet.graphics.Batch()

    def on_draw(self):
        self.clear()
        self.main_batch.draw()
