#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 11:44:18 2018

Problem 97:

The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457+1.

Find the last ten digits of this prime number.



@author: abocci
"""

import math

import time
#from mpmath import mp
#mp.dps = 50
#print(mp.quad(lambda x: mp.exp(-x**2), [-mp.inf, mp.inf]) ** 2)

## look for repetition in last 10 digits of 2^n
#for i in range(60):
#    p = mp.power(2,i)
#    ss = mp.nstr(p,30)
#    print('{:>2d} - {:>20s} - {:10s}'.format(i,ss[:-2],ss[-12:]))


t=time.time()

a = 28433
e = 7830457

x=a
N=e
_x = a

# if true, calculate the full value and compare with troncated, for validation
do_test = False

for i in range(N):
   _x *= 2  ## a * 2^N
   _xs = str(_x)
   if len(_xs)>12:
       _xs = _xs[-14:]
   ## now return a truncated _x 
   _x = float(_xs)

   continue

   if (do_test): 
       x *= 2  ## a * 2^N
       #xs = str(x)
       print('{:>2d} - {:>20s} - {:>14s}'.format(i,str(x),_xs)) 
   else:
       print('{:>2d} - {:>14s}'.format(i,_xs)) 
       
     
print('\nThe results is {}+1'.format(_xs[-12:-2]))    
print ("\nSolved in {:.5f} ms".format((time.time()-t)*1000))

