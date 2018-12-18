#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 20:32:30 2018

Problem:
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)

Solution:
    This is a generalization of the 

@author: abocci
"""

import numpy as np


def p36(min_num, max_num, base=2):
    # ---- Auxilary vectorization functions

    # invert object
    v_invert = np.vectorize(lambda x: str(x)[::-1])

    #  make integer from string in given base
    v_make_int = np.vectorize(lambda x, b: int(x, b))

    # vectorize binary representation
    if base == 2:
        v_repr_bin = np.vectorize(lambda x, base: np.binary_repr(x))
    else:
        # - Generalization (slower x25 for base2)
        v_repr_bin = np.vectorize(lambda x, base: np.base_repr(x, base))

    # vectorize removal of trailing zeros
    v_remove_tra0 = np.vectorize(lambda x: x.lstrip('0'))

    # ---- Start of analysis

    # Build first an array of integer and its palindrom
    p_b10 = np.arange(min_num, max_num)
    p_reverted_b10 = v_make_int(v_invert(p_b10), 10)

    p_b2 = v_repr_bin(p_b10, base)
    p_reverted_b2 = v_remove_tra0(v_invert(p_b2))

    # Comparing element wise the two pairs of arrays, 
    # give the palindromic list in each base

    palinrom_b10 = p_b10[p_b10 == p_reverted_b10]
    palinrom_b2 = p_b2[p_b2 == p_reverted_b2]

    # Find the common values

    p_b2_int_b10 = v_make_int(palinrom_b2, base)  # transform in int10 the bin list
    p_common = np.intersect1d(palinrom_b10, p_b2_int_b10)

    # Make the sum
    return np.sum(p_common)


print("Solution of Problem 36:", p36(1, 1000000, 2))
