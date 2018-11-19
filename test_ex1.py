#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:22:17 2018

@author: Anastasia
"""

#%%

from exercise_1 import checkout
def test_shoppingcart():
    values = []
    
    for item in values:
        assert checkout(item) == None

def test_shoppingcart1():
    values = [["guitar"]]
    
    for item in values:
        assert checkout(item) == 1000

def test_shoppingcart2():
    values = [["guitar", "guitar strings"]]
    
    for item in values:
        assert checkout(item) == 1010
