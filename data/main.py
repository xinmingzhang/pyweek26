import random
import string

import pyglet
from .components import SceneManager,Block
from .scenes import Title,Game

def screen_width():
    try:
        import ctypes
        user32 = ctypes.windll.user32
        s_w = user32.GetSystemMetrics(0)
        return s_w
    except:
        pass
    try:
        import pygame
        pygame.init()
        infos = pygame.display.Info()
        s_w = infos.current_w
        return s_w
    except:
        pass
    try:
        import AppKit
        screen = AppKit.NSScreen.screens()
        s_w = screen.frame().size.width
        return s_w
    except:
        pass



def main():
    try:
        sw = screen_width()
    except:
        sw = 800

    sm = SceneManager()
    sm.add_scene('game',Game(sm,sw))
    sm.add_scene('title',Title(sm,sw))

    pyglet.clock.schedule_interval(sm.update, 1 / 60.0)
    pyglet.app.run()



