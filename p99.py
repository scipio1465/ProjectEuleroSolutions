#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 17:15:12 2018

Problem 99:

Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.


@author: abocci
"""


import math as mmmm

def p99():
    c=0
    idx = 0
    alne_max = 1
    c=0
    with open('p099_base_exp.txt','r') as f:
        for line in f:
            c += 1
            #if (c<10):
            #    break
            a = line.split(',')[0]        
            e = line.split(',')[1]
            alne = float(e) * mmmm.log(float(a))
            if (alne > alne_max):
                idx=c    
                alne_max = alne
                #print(c,a,e,alne)
    print('The higher line is :',idx)            
    print('scanned {} lines'.format(c))
p99()
