#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:00:33 2018

Problem 33:

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting 
to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

@author: abocci
"""

# Imposing xy/yz = x/z
# the solution is: (10*x + y)*z = (10*y+z)*x
# with x < z

import itertools

import time
t=time.time()

range_digits = [[i for i in range(1,10)]]*3
[ print('{}{}/{}{} = {}/{}'.format(x,y,y,z,x,z)) for (x,y,z) in itertools.product(*range_digits) if ((10*x + y)*z == (10*y+z)*x and x<z)] 

#this is the end
print ("\nSolved in {:.2f} ms".format(1000*(time.time()-t)))