#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:22:38 2018

@author: Anastasia
"""

#%%
from exercise_1 import checkout_3

def test_shopping_cart1():
    values = ["guitar", "insurance"]
    
    for item in values:
        assert checkout_3(item,"gold") == 954,75

def test_shoppingcart2():
    values = ["guitar","insurance"]
    
    for item in values:
        assert checkout_3(item, "silver") == 994,7

def test_shoppingcart3():
    values = ["guitar","insurance"]  
    for item in values:
        assert checkout_3(item, "normal") == 1015