#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from metrics import coords, dist
from Ball import Ball

from .Wall import Wall


class BottomWall(Wall):

    def draw(self, window):
        x = self.pos[0] - self.half_len
        y = self.pos[1]
        p = coords( (x,y) )
        w = dist(self.width)
        h = dist(self.half_len*2)
        r = pygame.Rect( p, (h,w) )
        pygame.draw.rect(window, self.color, r)
        xy1 = ( self.pos[0]-self.half_len, self.pos[1] )
        xy2 = ( self.pos[0]+self.half_len, self.pos[1] )
        pygame.draw.line(window, (255,255,255), coords(xy1), coords(xy2), 2)


    def bang_detection(self, other):
        # other -- это шарик
        if not isinstance(other, Ball):
            return False
        # шарик не левее стенки и не правее ее
        if abs( self.pos[0] - other.pos[0] ) > self.half_len:
            return False
        # шарик летит вниз
        if other.vel[1] >= 0:
            return False
        # шарик сверху от стенки
        if other.pos[1] < self.pos[1]:
            return False
        # шарик коснулся стенки
        if other.pos[1] - other.radius > self.pos[1]:
            return False
        return True

    def bang_action(self, other):
        # Скорость шарика по вертикали меняется на противоположную
        vx = other.vel[0]
        vy = other.vel[1]
        other._change_vel( (vx,-vy) )

