#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 19:46:37 2018

@author: Anastasia
"""

#%%
from exercise_1 import checkout_2
def test_shopping_cart():
    values = []
    
    for item in values:
        assert checkout_2(item) == None

def test_shopping_cart1():
    values = [["guitar", "insurance"]]
    
    for item in values:
        assert checkout_2(item) == 1005

def test_shoppingcart2():
    values = [["guitar","insurance", "insurance", "priority mail", "priority mail"]]
    
    for item in values:
        assert checkout_2(item) == 1015