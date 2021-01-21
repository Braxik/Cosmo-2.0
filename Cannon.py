#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from math import sin, cos, radians
from metrics import coords, dist
from SpriteBullet import SpriteBullet
from Thing import Thing


class Cannon(Thing):
    def __init__(self, pos, angle=0.0, length=0.3, color=(255,255,255) ):
        super().__init__()
        self.__pos = pos
        self.__angle = angle
        self.__length = length
        self.__width = 0.1
        self.__color = color
        self.__turn = 0.0
        self.__bullet = 0.0
        self.__bullet_accel = 0.0
        self.heart = True

    @property
    def length(self):
        return self.__length
        
    @property
    def angle(self):
        return self.__angle

    @property
    def pos(self):
        return self.__pos

    @property
    def end(self):
        x2 = self.pos[0] + self.__length * cos(self.__angle)
        y2 = self.pos[1] + self.__length * sin(self.__angle)
        return (x2, y2)

    def turn_left(self):
        self.__turn = radians(30)
        x2 = self.pos[0] - 0.4
        y2 = self.pos[1]
        self.__pos = (x2, y2)
        
    def turn_right(self):
        self.__turn = - radians(30)
        x2 = self.pos[0] + 0.4
        y2 = self.pos[1]
        self.__pos = (x2, y2)

    def turn_up(self):
        self.__turn = radians(30)
        x2 = self.pos[0]
        y2 = self.pos[1] + 0.4
        self.__pos = (x2, y2)

    def turn_down(self):
        self.__turn = - radians(30)
        x2 = self.pos[0]
        y2 = self.pos[1] - 0.4
        self.__pos = (x2, y2)

    def turn_stop(self):
        self.__turn = 0.0
        
    def prepare(self):
        self.__bullet = 0.0
        self.__bullet_accel = 3.0
        
    def fire(self):
        vx = self.__bullet * cos(self.__angle)
        vy = self.__bullet * sin(self.__angle)
        bullet = SpriteBullet(pos=self.end, vel=(vx, vy), radius=0.05, filename='images.jpg')
        return bullet

    def move(self, delta_t):
        self.__bullet = self.__bullet + self.__bullet_accel * delta_t
        
    def draw(self, window):
        xy1 = coords(self.pos)
        xy2 = coords(self.end)
        pygame.draw.line(window, self.__color, xy1, xy2, dist(self.__width))

    def bang_action(self, other):
        x1 = self.__pos[0]
        y1 = self.__pos[1]
        x2, y2 = other.pos
        if x1 - 0.3 < x2 < x1 + 0.4 and y1 - 0.3 < y2 < y1 + 0.3:
            return True