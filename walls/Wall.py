#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from metrics import coords, dist

from Thing import Thing


class Wall(Thing):

    def __init__(self, length, pos, color=(128,128,128), width=0.1):
        super().__init__()
        self.__pos = pos
        self.__color = color
        self.__width = width
        self.__half_len = length / 2.0
        
    @property
    def width(self):
        return self.__width
        
    @property
    def pos(self):
        return self.__pos
        
    @property
    def color(self):
        return self.__color
        
    @property
    def half_len(self):
        return self.__half_len
        
    def move(self, dt):
        pass
        
    def draw(self, window):
        raise NotImplementedError()
        














