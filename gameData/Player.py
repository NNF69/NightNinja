# --------------------[Imports]--------------------------------
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from ursina.texture_importer import load_texture

# --------------------[player texture]-------------------------
playerTexture = load_texture(name= 'player.gif', path='assets\\player\\player')

# playerTexture = color.black10

# --------------------[level definition]-----------------------
def Player():
    
    # ____________________[player config]______________________
    player = PlatformerController2d(Texture= playerTexture)
    player.x=1
    player.y = raycast(player.world_position, player.down).world_point[1] + .01
    camera.add_script(SmoothFollow(target=player, offset=[0,5,-30], speed=4))

    # ____________________[input handlers]_____________________
    input_handler.bind('right arrow', 'd')
    input_handler.bind('left arrow', 'a')
    input_handler.bind('up arrow', 'space')
    input_handler.bind('gamepad dpad right', 'd')
    input_handler.bind('gamepad dpad left', 'a')
    input_handler.bind('gamepad a', 'space')

    player.add_script(NoclipMode2d())
    return player