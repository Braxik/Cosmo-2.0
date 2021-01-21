#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from Cannon import Cannon
from metrics import dist, coords
from os.path import join, abspath
from math import degrees


class SpriteCannon(Cannon):

    def __init__(self, pos, angle=0.0, length=0.3, filename='cannon.png'):
        super().__init__(pos, angle=angle, length=length)
        self.__filepath = join('resources',filename)
        self.__filepath = abspath(self.__filepath)
        self.__image = None
        
    def load_image(self):
        im = pygame.image.load(self.__filepath)
        w = dist(self.length*2)
        h = w * im.get_height() // im.get_width()
        self.__image = pygame.transform.smoothscale( im, (w,h) )
        
    def draw(self, window):
        if self.__image is None:
            self.load_image()
        p = coords(self.pos)
        a = degrees(self.angle)
        im = pygame.transform.rotate(self.__image, a)
        x = p[0] - im.get_width()//2
        y = p[1] - im.get_height()//2
        p = (x,y)
        window.blit(im, p)