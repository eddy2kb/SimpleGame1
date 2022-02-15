from ursina import *
import sys
import os
import PIL
from ursina.prefabs.first_person_controller \
     import FirstPersonController
import time

app = Ursina()
Slope1 = Entity(model='plane', texture='res/driedMud1.png', collider='mesh',
                scale=(40,1,40),
                rotation=(16,0,0)
                )
ground1 = Entity(model='plane', texture='res/bricks1.png', collider='box',
                scale=(40,1,40),
                )
ground2 = Entity(model='plane', texture='res/bricks1.png', collider='box',
                scale=(40,1,30),
                position=(0, 5.52, -34)
                )

player = FirstPersonController()
player.speed = 15
player.disable()
player.enable()

Sky()

app.run()
