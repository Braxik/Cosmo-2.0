#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Thing import Thing
from Ball import Ball
from Cannon import Cannon
from Bullet import Bullet
from walls import *


disallowed_bangs = [
    (Ball, Bullet),
]
# 1. Получается, что пулька не сталкивается с пулькой.


allowed_bangs = [
    (Wall,   Thing),
    (Bullet, Ball),
    (Ball,   Ball),
]
# 1. Может ли стенка сталкиваться с пушкой?
# 2. Может ли пулька сталкиваться с пушкой?


def bang_allowed(b1, b2):
    for type1, type2 in disallowed_bangs:
        if isinstance(b1, type1) and isinstance(b2, type2):
            return False
    for type1, type2 in allowed_bangs:
        if isinstance(b1, type1) and isinstance(b2, type2):
            return True
    return False


def bang_pairs(all_things: list):
    prev = []   # Список предыдущих столкновений
    for b1 in iter(all_things):
        if b1.dead:
            continue
        for b2 in iter(all_things):
            if b2.dead:
                continue
            if b1 is b2:
                continue
            if not bang_allowed(b1, b2):
                continue
            # Не встречалась ли раньше пара ( b2, b1 )?
            p = (id(b2), id(b1))
            if p not in prev:
                p1 = (id(b1), id(b2))
                prev.append(p1)
                yield (b1, b2)