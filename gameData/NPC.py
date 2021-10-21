from ursina import *
from gameData.Player import Player

enemy_texture = color.red

player = Player()

def NPC(player):
    def block(x,y):
        block = Entity(
            model = 'quad',
            collider = 'box',
            scale = (3, 5),
            position = (x,y),
            color = enemy_texture,
        )
        return block

    em1 = block(4,6)
    # em1.add_script(SmoothFollow(target=player, offset=[0,5,-30], speed=4))


