#!/usr/bin/env python3
# -*- coding: utf-8 -*-

window_size = (640, 490)

pixels_per_meter = 100

# Функция, которая пересчитывает расстояние в метрах
# в расстояние в пикселях
def dist(s):
    return round(s * pixels_per_meter)

# Функция, которая пересчитывает координаты в метрах
# в координаты в пикселях
def coords(p):
    x = dist(p[0])
    y = dist(p[1])
    y = window_size[1] - y
    return (x, y)