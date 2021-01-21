#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from random import uniform, gauss
import os
from os import path
import sys
from metrics import window_size, coords, dist
from walls import *
from bang_pairs import bang_pairs
from SpriteBall import SpriteBall
from SpriteCannon import SpriteCannon
from Explosion import Explosion
clock = pygame.time.Clock()
FPS = 50


class Scene(object):

    def __init__(self):
        self.__things = []
        self.__total_time = None
        self.__delta_t = None
        self.__window = None
        self.__game_continues = None
        self.start = True
        self.heart = True
        self.tt = []
        self.kol = 0
        self.end_the_game = True
        self.cords = []
        self.kol_balls = 0

    @property
    def things(self):
        return iter(self.__things)

    def win(self):
        if self.heart:
            flags = pygame.DOUBLEBUF | pygame.RESIZABLE
            self.__window = pygame.display.set_mode((640, 490), flags)
            font = pygame.font.Font(None, 50)
            text = font.render("WIN!!", True, (100, 255, 100))
            text1 = font.render("Нажмите R чтобы продолжить", True, (100, 255, 100))
            text_x = 640 // 2 - text.get_width() // 2
            text_y = 490 // 2 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            self.__window.blit(text, (text_x + 10, text_y))
            pygame.draw.rect(self.__window, (0, 255, 0), (text_x, text_y - 10,
                                                          text_w + 20, text_h + 20), 1)
            self.__window.blit(text1, (text_x - 215, text_y + 65))
            pygame.draw.rect(self.__window, (0, 255, 0), (text_x - 220, text_y + 45,
                                                          text_w + 440, text_h + 20), 1)
            run = True
            sound = 1
            while run:
                if sound == 1:
                    shoot_sound = pygame.mixer.Sound('win.mp3')
                    shoot_sound.play()
                    sound = 2
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.finalize()
                    if event.type == pygame.KEYDOWN:
                        if event.key == 114:
                            shoot_sound.set_volume(0.0)
                            run = False
                            self.__things = []
                            self.tt = []
                            self.kol = 0
                            self.end_the_game = True
                            self.heart = False
                            self.leftwall_bang = LeftWall.kol_bangs_end(10)
                            self.start = False
                            self.kol_balls = 0
                            self.load()
                            self.run()
                            self.kol = 0
                pygame.display.flip()

    def ended(self):
        if self.heart:
            flags = pygame.DOUBLEBUF | pygame.RESIZABLE
            self.__window = pygame.display.set_mode((640, 490), flags)
            font = pygame.font.Font(None, 50)
            text = font.render("Game Over", True, (100, 255, 100))
            text1 = font.render("Нажмите R чтобы продолжить", True, (100, 255, 100))
            text_x = 640 // 2 - text.get_width() // 2
            text_y = 490 // 2 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            self.__window.blit(text, (text_x + 10, text_y))
            pygame.draw.rect(self.__window, (0, 255, 0), (text_x, text_y - 10,
                                                       text_w + 20, text_h + 20), 1)
            self.__window.blit(text1, (text_x - 150, text_y + 65))
            pygame.draw.rect(self.__window, (0, 255, 0), (text_x - 150, text_y + 45,
                                                          text_w + 335, text_h + 20), 1)

            run = True
            sound = 1
            while run:
                if sound == 1:
                    shoot_sound = pygame.mixer.Sound('lase.mp3')
                    shoot_sound.play()
                    sound = 2
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.finalize()
                    if event.type == pygame.KEYDOWN:
                        if event.key == 114:
                            shoot_sound.set_volume(0.0)
                            run = False
                            self.__things = []
                            self.tt = []
                            self.kol = 0
                            self.end_the_game = True
                            self.heart = False
                            self.leftwall_bang = LeftWall.kol_bangs_end(10)
                            self.start = False
                            self.load()
                            self.run()
                            self.kol = 0
                pygame.display.flip()

    def add_thing(self, new_thing, as_first=False):
        # Тут, если необходимо, проверить,
        # можно ли добавлять предмет на сцену
        if as_first:
            self.__things.insert(0, new_thing)
        else:
            self.__things.append(new_thing)
    
    def load(self):
        if self.start is False:
            '''
                Устанавливает исходные данные игры.
            '''
            for k in range(0, 5):
                x = uniform(6.0, 15.0)
                y = uniform(1.0, 4.3)
                vx = -1
                vy = 0
                b = SpriteBall(pos=(x, y), vel=(vx, vy),
                               radius=0.3, filename='ggggg.png' )
                self.add_thing(b)
                self.tt.append(b)

            # Ставим стенку слева
            lw = LeftWall(length=4.0, pos=(0.5, 2.5))
            self.add_thing(lw)
            self.posit_l = (0.5, 2.5)

            # Ставим стенку сверху
            tw = TopWall(length=6, pos=(3.5, 4.5))
            self.add_thing(tw)
            self.posit_u = (3.5, 4.5)

            # Ставим стенку снизу
            bw = BottomWall(length=6, pos=(3.5, 0.5))
            self.add_thing(bw)
            self.posit_d = (3.5, 0.5)

            rw = RightWall(length=4, pos=(6.5, 2.5))
            self.add_thing(rw)
            self.posit_d = (3.5, 0.5)

            # Ставим на сцену пулемет
            c = SpriteCannon(pos=(1.0, 2.5), length=0.3)
            self.add_thing(c)
            self.left = self.__things[5]
            self.__cannon = c
            self.heart = True
        
    def initialize(self):
        pygame.init()
        self.__total_time = pygame.time.get_ticks()
        #flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
        flags = pygame.DOUBLEBUF | pygame.RESIZABLE
        self.__window = pygame.display.set_mode(window_size, flags)
        self.__game_continues = True
        Explosion.load_image()

    def finalize(self):
        pygame.quit()

    def load_image(name, colorkey=None):
        fullname = os.path.join("fon.jpg")
        image = pygame.image.load(fullname)
        return image

    def start_screen(self):
        pygame.init()
        flags = pygame.DOUBLEBUF | pygame.RESIZABLE
        self.__window = pygame.display.set_mode(window_size, flags)
        intro_text = ["                                           Cosmo 2.0",
                      "                                        Правила игры:",
                      "                                 Сбить все астероиды",
                      "Управление:",
                      "             w, s, a, d",
                      "Стрельба:",
                      "             Space"]

        fon = pygame.transform.scale(self.load_image('fon.jpg'), (640, 490))
        self.__window.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.__window.blit(string_rendered, intro_rect)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finalize()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    run = False
                    self.start = False
                    self.load()
                    self.run()
            pygame.display.flip()

    @property
    def game_continues(self):
        return self.__game_continues

    def game_over(self):
        self.__game_continues = False
        
    # Эта функция нам будет особенно интересна!!!!!
    def take_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over()
            elif event.type == pygame.KEYDOWN:
                if event.key == 97:
                    # Пушка начинает вращение против часовой стрелки
                    if self.__cannon.pos[0] - 0.5 > self.posit_l[0]:
                        self.__cannon.turn_left()
                elif event.key == 100:
                    if self.__cannon.pos[0] + 0.5 < 6.5:
                        self.__cannon.turn_right()
                elif event.key == 119:
                    if self.__cannon.pos[1] + 0.4 < self.posit_u[1]:
                        self.__cannon.turn_up()
                elif event.key == 115:
                    if self.__cannon.pos[1] - 0.5 > self.posit_d[1]:
                        self.__cannon.turn_down()
                elif event.key == 32:
                    # Начинаем подготовку к выстрелу
                    self.__cannon.prepare()
            elif event.type == pygame.KEYUP:
                if event.key == 97 or event.key == 100:
                    # Пушка остановилась
                    self.__cannon.turn_stop()
                elif event.key == 32:
                    # Стреляем
                    bullet = self.__cannon.fire()
                    self.add_thing(bullet, as_first=True)
                    shoot_sound = pygame.mixer.Sound('iu.mp3')
                    shoot_sound.play()
        self.leftwall_bang = LeftWall.kol_bangs(10)
        for bang in self.__things:
            a = self.__cannon.bang_action(bang)
            if self.leftwall_bang > 0:
                a = True
            if bang in self.tt and a:
                self.start = 1
                self.run()
        for balls in self.tt:
            if balls not in self.__things:
                self.kol += 1
                ind = self.tt.index(balls)
                del self.tt[ind]
                break
        if self.kol == 5:
            self.start = 2
            self.run()

    def detect_time(self):
        # Сколько времени прошло с прошлого кадра
        t1 = pygame.time.get_ticks()
        self.__delta_t = ( t1 - self.__total_time ) / 1000.0
        self.__total_time = t1

    def move(self):
        amount = self.__delta_t
        while amount > 0.01:
            self.do_move(0.01)
            amount = amount - 0.01
        if amount > 0:
            self.do_move(amount)

    def do_move(self, dt):
        new_things = []
        for b1, b2 in bang_pairs(self.__things):
            new = b1.bang(b2)
            if new is not None:
                new_things = new_things + new
        self.__things += new_things
        
        for b in self.things:
            b.move(dt)

    def draw(self):
        self.__window.fill( (0,0,0) )
        for b in self.things:
            b.draw(self.__window)
        pygame.display.flip()

    def remove(self):
        '''
            Удаляет со сцены лишние объекты
        '''
        new = [b for b in self.__things if not b.dead]
        self.__things = new

    def run(self):
        if self.start is True:
            self.start_screen()
        elif self.start == 1:
            self.ended()
        elif self.start == 2:
            self.win()
        elif self.start is False or self.start != 1 or self.start != 2:
            self.initialize()
            try:
                while self.game_continues:
                    self.take_events()
                    self.detect_time()
                    self.move()
                    self.remove()
                    self.draw()
            finally:
                self.finalize()
