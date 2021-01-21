#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from metrics import coords, dist
from Ball import Ball
from Explosion import Explosion
from .Wall import Wall
from SpriteBall import SpriteBall
kol_bang1 = 0


class LeftWall(Wall):
    def draw(self, window):
        x = self.pos[0] - self.width
        y = self.pos[1] + self.half_len
        p = coords((x,y))
        w = dist(self.width)
        h = dist(self.half_len*2)
        r = pygame.Rect( p, (w,h) )
        pygame.draw.rect(window, self.color, r)
        xy1 = ( self.pos[0], self.pos[1]+self.half_len )
        xy2 = ( self.pos[0], self.pos[1]-self.half_len )
        pygame.draw.line(window, (255,255,255), coords(xy1), coords(xy2), 2)

    def kol_bangs(self):
        global kol_bang1
        return kol_bang1

    def kol_bangs_end(self):
        global kol_bang1
        kol_bang1 = 0
        return kol_bang1

    def bang_detection(self, other):
        # other -- это шарик
        if not isinstance(other, Ball):
            return False
        # шарик не выше стенки и не ниже ее
        if abs( self.pos[1] - other.pos[1] ) > self.half_len:
            return False
        # шарик летит влево
        if other.vel[0] >= 0:
            return False
        # шарик справа от стенки
        if other.pos[0] < self.pos[0]:
            return False
        # шарик коснулся стенки
        if other.pos[0] - other.radius > self.pos[0]:
            return False
        return True

    def bang_action(self, other):
        global kol_bang1
        other.kill()
        x = (self.pos[0] + other.pos[0]) / 2
        y = (self.pos[1] + other.pos[1]) / 2
        exp = Explosion(pos=(x, y))
        shoot_sound = pygame.mixer.Sound('vz.mp3')
        shoot_sound.play()
        kol_bang1 += 1
        return [exp]