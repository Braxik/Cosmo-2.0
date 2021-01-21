#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from Bullet import Bullet
from os.path import join, abspath
from metrics import dist, coords


class SpriteBullet(Bullet):

    def __init__(self, pos, vel, radius, filename="images.jpg", mass = 0.1):
        super().__init__(pos, vel, radius=radius, mass=mass, color=(255,255,255))
        path = join('resources', filename)
        self.__filepath = abspath(path)
        self.__image = None
        
    def load_image(self):
        im = pygame.image.load(self.__filepath)
        d = dist( self.radius * 2 )
        self.__image = pygame.transform.smoothscale( im, (d,d) )
        
    def draw(self, window):
        if self.__image is None:
            self.load_image()
        # Тут нарисуем наш шарик по-новому
        p = coords(self.pos)
        x = p[0] - self.__image.get_width() // 2
        y = p[1] - self.__image.get_height() // 2
        p = ( x, y )
        window.blit(self.__image, p )