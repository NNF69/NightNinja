# --------------------[Imports]--------------------------------
from ursina import *
from gameData.levels.scene1 import tryHarder
from gameData.Player import Player
from gameData.NPC import NPC


def NightNinja():

# --------------------[window/camera config]-------------------
    window.borderless = False
    app = Ursina()
    window.color = color.light_gray
    camera.orthographic = True
    camera.fov = 23

# --------------------[update]-----------------
    def update():
        pass



# --------------------[level/player definition]-----------------
    tryHarder()
    player = Player()
    NPC()

    


    return app