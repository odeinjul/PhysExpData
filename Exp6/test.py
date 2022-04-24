#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib
from physicsexp.mainfunc import *
import matplotlib as mpl
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'SimHei'
mpl.rcParams['axes.unicode_minus'] = False

fin = open('./data.txt', 'r', encoding='utf-8')
j = readoneline(fin)
l_j = readoneline(fin)
i = readoneline(fin)
l_i = readoneline(fin)
fin.close()

print('h_1:\t',j)
print('t:\t',l_j)

slope, intercept = simple_linear_plot(j, l_j, xlab='序号$s$', ylab='相应位置$m/s^2$',
                                      title='序号与相应位置拟合曲线', save='1.png')
print('lambda:\t',slope * 2)

print('h_1:\t',i)
print('t:\t',l_i)

slope, intercept = simple_linear_plot(i, l_i, xlab='序号$s$', ylab='相应位置$m/s^2$',
                                      title='序号与相应位置拟合曲线', save='2.png')
print('lambda:\t',slope *2)
print