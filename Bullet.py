#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from random import gauss, randint
from Ball import Ball
from Explosion import Explosion
from os.path import join, abspath
from metrics import dist, coords
from SpriteBall import SpriteBall


class Bullet(Ball):

    def __init__(self, pos, vel, radius=0.05, color=(0,0,255), mass=0.02 ):
        super().__init__(pos, vel, radius, color, mass)

    def bang_action(self, other):
        e = self.energy + other.energy
        if e < 0.01:
            return super().bang_action(other)
        else:
            self.kill()
            other.kill()
            x = (self.pos[0] + other.pos[0]) / 2
            y = (self.pos[1] + other.pos[1]) / 2
            exp = Explosion(pos=(x, y))
            shoot_sound = pygame.mixer.Sound('vz.mp3')
            shoot_sound.play()
            return [exp]
