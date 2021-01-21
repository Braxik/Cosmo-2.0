#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from metrics import coords, dist
from math import sqrt

from Thing import Thing


class Ball(Thing):

    def __init__( self, pos, vel, radius, color=(255,255,255), mass=0.1 ):
        super().__init__()
        self.__pos = pos
        self.__vel = vel
        self.__radius = radius
        self.__color = color
        self.__mass = mass
        
    @property
    def energy(self):
        vx = self.vel[0]
        vy = self.vel[1]
        e = self.__mass * ( vx**2 + vy**2 ) / 2
        return e
        
    @property
    def mass(self):
        return self.__mass
        
    @property
    def radius(self):
        return self.__radius
        
    @property
    def pos(self):
        return self.__pos
        
    @property
    def vel(self):
        return self.__vel
        
    def _change_vel(self, new_vel):
        self.__vel = new_vel
        
    def move(self, dt):
        x = self.__pos[0]
        vx = self.__vel[0]
        x = x + vx*dt
        y = self.__pos[1]
        vy = self.__vel[1]
        y = y + vy*dt
        self.__pos = (x,y)
        return None # можно не писать
        
    def draw(self, window):
        win_pos = coords(self.__pos)
        win_rad = dist(self.__radius)
        pygame.draw.circle(window, self.__color, win_pos, win_rad)
        
    def bang_detection(self, other):
        if not isinstance(other, Ball):
            return False
        x1 = self.__pos[0]
        y1 = self.__pos[1]
        x2 = other.__pos[0]
        y2 = other.__pos[1]
        dx = x2 - x1
        dy = y2 - y1
        r = sqrt( dx**2 + dy**2 )
        if r > self.__radius + other.__radius:
            return False
        dt = 0.001
        x1 = x1 + self.__vel[0]*dt
        y1 = y1 + self.__vel[1]*dt
        x2 = x2 + other.__vel[0]*dt
        y2 = y2 + other.__vel[1]*dt
        dx = x2 - x1
        dy = y2 - y1
        r2 = sqrt( dx**2 + dy**2 )
        if r2 >= r:
            return False
        return True
        
    def bang_action(self, other):
        dx = other.__pos[0] - self.__pos[0]
        dy = other.__pos[1] - self.__pos[1]
        r = sqrt( dx**2 + dy**2 )
        cos_a = dx / r
        sin_a = dy / r
        vx1 =   self.__vel[0] * cos_a + self.__vel[1] * sin_a
        vy1 = - self.__vel[0] * sin_a + self.__vel[1] * cos_a
        vx2 =   other.__vel[0] * cos_a + other.__vel[1] * sin_a
        vy2 = - other.__vel[0] * sin_a + other.__vel[1] * cos_a
        vxc = ( self.__mass * vx1 + other.__mass * vx2 )
        vxc = vxc / ( self.__mass + other.__mass )
        vx1 = vx1 - vxc
        vx2 = vx2 - vxc
        vx1_new = other.__mass * vx2 / self.__mass
        vx2_new = self.__mass * vx1 / other.__mass
        vx1 = vx1_new + vxc
        vx2 = vx2_new + vxc
        self.__vel = (
            vx1 * cos_a - vy1 * sin_a ,
            vx1 * sin_a + vy1 * cos_a
        )
        other.__vel = (
            vx2 * cos_a - vy2 * sin_a ,
            vx2 * sin_a + vy2 * cos_a
        )