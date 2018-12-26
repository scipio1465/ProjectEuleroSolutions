#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 18:15:03 2018

Problem 99:
    
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.


@author: abocci
"""

import time

def make_squares(N):
    ## make a list of squares with N digits
    ll = []
    start = sqrt(10**(N-1))
    p = int(start)+1
    #print('start',N,p)
    while (len(str(p*p)) == N) :     
        ll.append(p*p)
        p += 1
    return ll

def make_dict_words(file):
    ## make a dictionary of the given words with key as numbers of letters
    D_words = {}
    with open(file,'r') as f:
        ## Put words in a list (cleaning)
        words_list = f.readlines()[0]
        words_list = words_list.replace('"','')
        words = words_list.split(",")
        
        ## Dictionary of words based on length
        for w in words:
            l = len(w)
            if l in D_words:
                D_words[l].append(w)
            else:
                D_words[l] = [w]
    return D_words


def make_anagram_pairs(w):
    # take words list with same lenght and
    # return list of pairs that are anagrams of each others
    anagrams_n = []    
    ## copy the list
    words_list = w[:]
    while len(words_list):
        w1 = words_list.pop(0)
        anagrams_w1 = [w1] ## list of anagrams of w1
        # dictionary of letters with frequency
        freq_w1= {k:w1.count(k) for k in set(w1)}
        for w2 in words_list:
            freq_w2= {k:w2.count(k) for k in set(w2)}
            if (freq_w1 == freq_w2): # w1 and w2 are anagrams
                anagrams_w1.append(w2)
                words_list.remove(w2) # remove w2 from the list to check
        ## add the set of anagrams of w1 to the anagram_pairs
        if (len(anagrams_w1)>1):
            anagrams_n.append(anagrams_w1)
    return anagrams_n

def check_good_encoder(w,i):
    ## w is a word with n letters
    ## i is a number with n digit
    ## the encoder associate letter to digit, in ordered manner
    ## An invalid encoder is ARISE and 99225 (9 assigned to A and R)
    
    ll = 10*['']
    valid = True
    for d,l in zip(str(i),w): 
        k = ll[int(d)]
        if not k:
            ll[int(d)] = l
        elif l in set(k):
            ll[int(d)] += l
        else:
            ll[int(d)] += l
            valid = False
    
    return valid
    
    
def match(squares,a_w_l,i):
    ## a_w_l : list of anagrams words (2 or more)
    ## i: square with the same length of words in a_w_l
    ## return pairs that can be encoded in squares, with same encoding
    ##
    ## Note: I need to encode all words with the same i
    ## for example CARE with 7056 and then RACE with 7056
    ## Sometime it is symmetric: 
    ## encoding ( NOTE 9216 ) --> testing: TONE 1296 ['NOTE', 'TONE']
    ## encoding ( TONE 9216 ) --> testing: NOTE 1296 ['NOTE', 'TONE']
    ## Sometime is not:
    ## encoding ( MEAN 9604 ) --> testing: NAME 4096 ['MEAN', 'NAME']
    ## encoding ( NAME 9604 ) --> testing: MEAN 0469 NOO!
    
    w_list = a_w_l[:]


    for w1 in a_w_l:
        # check if i is a good encoder for w1, otherwise skip
        # a good encoder is when different letter have different digital value
        if not check_good_encoder(w1,i): continue
        
        ## --> encoding (w1,i)        
        w_l_transformed = [] ## final collection to be filled
        for k in w_list: ## testing k-word with (w1,i) encoding
            if k != w1:  ## remove w1
                w2 = k[:] 
                for digit,letter in zip(str(i),w1): # transform with w1-i encoder
                    k = k.replace(letter,digit)
                
                #given the (w1-i) encoder, check if k is a square on its own
                if int(k) in squares:
                    ana_square = w1,i,w2,int(k) ## this is a pair we look for
                    w_l_transformed.append(ana_square)

        return w_l_transformed
        
    
def p98():
    D_words = make_dict_words('p098_words.txt')

    ## For each set of words, make a dictionary with squares words only, with len(word) as key
    ana_squares = []
    for (n,words_n) in D_words.items():
        squares = make_squares(n)
        ## now I have in a given n, words_n and sqaures
        ## build all pairs of anagrams
        anagrams_n = make_anagram_pairs(words_n)
        
        ## Loop over all squares, i: 
        ## and for a given anagram set, like ['EAST', 'SEAT'], I find a match, i.e.
        ## if those words are actually squares, with one of them being i, the other being another one
        for i in squares:
            for a_w_list in anagrams_n:
                a = match(squares,a_w_list, i)
                if a : ana_squares.append(a)

    p=ana_squares
    for i in p:
        print(i)

t=time.time()
p98()
print ("\nSolved in {}s".format(time.time()-t))
