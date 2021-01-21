#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from metrics import coords, dist
from Ball import Ball
from SpriteBall import SpriteBall
from .Wall import Wall


class RightWall(Wall):

    def draw(self, window):
        x = self.pos[0]
        y = self.pos[1] + self.half_len
        p = coords( (x,y) )
        w = dist(self.width)
        h = dist(self.half_len*2)
        r = pygame.Rect( p, (w,h) )
        pygame.draw.rect(window, self.color, r)
        xy1 = ( self.pos[0], self.pos[1]+self.half_len )
        xy2 = ( self.pos[0], self.pos[1]-self.half_len )
        pygame.draw.line(window, (255,255,255), coords(xy1), coords(xy2), 2)

    def bang_detection(self, other):
        # other -- это шарик
        if not isinstance(other, Ball):
            return False
        # шарик не выше стенки и не ниже ее
        if abs( self.pos[1] - other.pos[1] ) > self.half_len:
            return False
        # шарик летит вправо
        if other.vel[0] <= 0:
            return False
        # шарик слева от стенки
        if other.pos[0] > self.pos[0]:
            return False
        # шарик коснулся стенки
        if other.pos[0] + other.radius < self.pos[0]:
            return False
        return True

    def bang_action(self, other):
        # Скорость шарика по горизонтали меняется на противоположную
        if other is SpriteBall:
            vx = other.vel[0]
            vy = other.vel[1]
            if other.pos[0] < 6.6 and other.pos[1] < 5:
                other._change_vel((-vx, vy))
