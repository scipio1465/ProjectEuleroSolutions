#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 21:12:02 2018

Project Euler, p31


@author: abocci
"""
import numpy as np
import itertools

## Total money value
money = 200

## Total number of coins
coins = np.array([1,2,5,10,20,50,100,200])

## Coins splits (two groups)
k=2 # first k-coins and the rests
coins1 = coins[:k]
coins2 = coins[k:]

def num_combination(N,coins):

    ## max number of each coins of each kind to make 200p (2 pounds)
    max_coins = N/coins
    max_coins +=1

    ## Make a list of arange using the max number of coins
    list_range = [np.arange(int(i)) for i in max_coins]

    ## I use the itertools.product that does the cartesian product
    ## I will do for all combination of coins
    ## Then I put a constraint that the sum (weighted for the coin value) must be 200

    a = np.array([x for x in itertools.product(*list_range) if np.sum(x*coins)==N ])
    return len(a)

# final counter
tot_combination = 0

for N in range(0,money+1):
    # first group
    n_comb1 = num_combination(N,coins1)
    # second group on 200-N
    n_comb2 = num_combination(money-N,coins2)
    tot_combination += (n_comb1*n_comb2)
    print("For the split {}-{}: small have {} and large have {}. The total is {}".format(N,money-N,n_comb1,n_comb2,n_comb1*n_comb2))

print("The total combination is {}".format(tot_combination))

