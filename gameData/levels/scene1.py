# --------------------[Imports]--------------------------------
from ursina import *


# --------------------[level texture]--------------------------
ground_texture = color.olive.tint(-.4)
wall_texture = color.black
block_texture = color.brown


# --------------------[level definition]-----------------------
def tryHarder():

    # ____________________[ground]_____________________________
    ground = Entity(
        model = 'cube',
        color = ground_texture,
        z = -.1,
        y = -1,
        origin_y = 1,
        scale = (75, 10, 10),
        collider = 'box',
        ignore = True,
    )
    def Wall(x,y):
        wall = Entity(
            model = 'quad',
            color = wall_texture,
            scale = (5, 100),
            position = (x,y),
            collider = 'box'
        )
        return wall

    def block(x,y):
        block = Entity(
            model = 'quad',
            collider = 'box',
            scale = (5, 1),
            position = (x,y),
            color = block_texture,
            texture = 'brick'
        )
        return block



            

    wallLeft = Wall(-20, 0)
    wallRight = Wall(20,0)

    block_1 = block(-15, 5)
    block_2 = block(15, -2)
    block_3 = block(-1, 2)
