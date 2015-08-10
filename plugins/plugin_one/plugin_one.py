__author__ = 'Graham Voysey'
from plugins.plugin_one.itestplugin import ITestPlugin
from core import pyglet_window, pyglet_text, pyglet_sprite, unlockstate
from pyglet import graphics, app, text, window
import pyglet
import logging


class PluginOne(ITestPlugin):
    def print_status(self):
        print("Plugin registration status: operational!")

    def start(self):
        # start pyglet
        # appwindow = pyglet_window.PygletWindow(signal=None)
        # appwindow.set_fullscreen(fullscreen=True)
        if True:
            batch = graphics.Batch()
            canvas = pyglet_window.Canvas(batch, 200, 200)
            #  model = unlockstate.UnlockState()
            #  model.start()
            #  label = pyglet_text.PygletLabel(model, canvas, "Hello, World", canvas.xcenter(), canvas.ycenter())
            appwindow = pyglet_window.PygletWindow(signal=None, fullscreen=False)
            appwindow.batches.add(batch)
            appwindow.views.append(pyglet_text.PygletDynamicTextLabel(None, canvas, 'Hello, world',
                                                                      x=appwindow.width // 2,
                                                                      y=appwindow.height // 2,
                                                                      ))
            #  appwindow.views.append(label)
            #  appwindow.canvas = canvas
            #  label.render()
            #  appwindow.activate()
            appwindow.render()
            appwindow.start()
        if False:
            window = pyglet.window.Window()
            label = pyglet.text.Label('Hello, world',
                                      font_name='Times New Roman',
                                      font_size=36,
                                      x=window.width // 2, y=window.height // 2,
                                      anchor_x='center', anchor_y='center')

            @window.event
            def on_draw():
                window.clear()
                label.draw()

            pyglet.app.run()

        logging.log(logging.INFO, "done!")
        # window.start()
