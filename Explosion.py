#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from Thing import Thing
from os.path import join, abspath
from metrics import dist, coords


class Explosion(Thing):
    __filename__ = 'explosion.png'
    __size__ = 256
    __rows__ = 6
    __cols__ = 8
    __count__ = __rows__ * __cols__
    __image = None

    def __init__(self, pos, width=0.5, duration=2.0):
        super().__init__()
        self.__pos = pos
        self.__width = width
        self.__duration = duration
        self.__alive = 0.0
        self.ttt = []

    def tt(self):
        return self.ttt
    
    @property
    def current_image(self):
        index = int( self.__alive / self.__duration * self.__count__ )
        if index >= self.__count__:
            index = self.__count__ - 1
        r = index // self.__cols__
        c = index % self.__cols__   # остаток от деления
        x = self.__size__*c
        y = self.__size__*r
        rect = pygame.Rect( (x,y), (self.__size__,self.__size__) )
        im = self.__image.subsurface( rect )
        w = dist(self.__width)
        # Тут надо сжать картинку до нужного размера
        return pygame.transform.smoothscale(im, (w,w))
        
    @property
    def pos(self):
        return self.__pos
        
    @property
    def width(self):
        return self.__width
        
    @property
    def duration(self):
        return self.__duration

    def move(self, delta_t):
        self.__alive = self.__alive + delta_t
        if self.__alive > self.__duration:
            self.kill()

    @classmethod
    def load_image(self):
        path = join('resources', Explosion.__filename__)
        path = abspath(path)
        Explosion.__image = pygame.image.load(path)

    def draw(self, window):
        if self.__image is None:
            self.load_image()
        p = coords(self.pos)
        k = 1
        im = self.current_image
        x = p[0] - im.get_width() // 2
        y = p[1] - im.get_height() // 2
        p = (x,y)
        window.blit(im, p)