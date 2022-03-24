#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib
from physicsexp.mainfunc import *
from physicsexp.gendocx import *
import matplotlib as mpl
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'SimHei'
mpl.rcParams['axes.unicode_minus'] = False

fin = open('data.txt', 'r', encoding='utf-8')
r = readoneline(fin)
T1 = readoneline(fin)
fin.close()

print('r:\t',r)

T = T1/30
print('T:\t',T)

pi = 3.1415926
temp1 = 9.8*r/(4*pi*pi)
temp2 = temp1*T*T
temp3 = r*r
Ic = temp2 - temp3
m=15/1000

Ic *= (2*m)

print('Ic:\t',Ic)