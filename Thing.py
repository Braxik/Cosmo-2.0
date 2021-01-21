#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Thing(object):

    def __init__(self):
        self.__dead = False
        
    @property
    def dead(self):
        return self.__dead
        
    def kill(self):
        self.__dead = True

    def move(self, dt):
        raise NotImplementedError()
        
    def draw(self, dt):
        raise NotImplementedError()
        
    # Было ли столкновение?
    def bang_detection(self, other):
        return False
        
    # Что произошло в результате столкновения?
    def bang_action(self, other):
        return None
        
    def bang(self, other):
        if self is other: return None
        if self.dead or other.dead: return None
        if self.bang_detection(other):
            return self.bang_action(other)
        return None