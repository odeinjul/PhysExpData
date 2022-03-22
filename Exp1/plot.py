#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib
from physicsexp.mainfunc import *
from physicsexp.gendocx import *
import matplotlib as mpl
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'SimHei'
mpl.rcParams['axes.unicode_minus'] = False

fin = open('./data.txt', 'r', encoding='utf-8')
h = readoneline(fin)
t = readoneline(fin)
fin.close()

print('h_0:\t',h)

h = h/t

print('h_1:\t',h)
print('t:\t',t)

slope, intercept = simple_linear_plot(t, h, xlab='两光电门时间差$s$', ylab='光电门间平均速度$m/s^2$',
                                      title='重力加速度线性拟合曲线', save='1.png')
slope *= 2
print('g:\t',slope)