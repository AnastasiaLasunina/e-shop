#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:28:10 2018

@author: Anastasia
"""
#%% ex. 1
shoppinglist = {
            "guitar": 1000, 
            "pick box": 5, 
            "guitar strings": 10
            }
shoppingcart = ["guitar", "pick box"]
def checkout(shoppingcart):
    finalprice = 0
    if shoppingcart == []:
        return None
    else:
        for item in shoppingcart:
            finalprice = finalprice + (shoppinglist[item])
    return finalprice
        

#%% ex.2 
#Blue Belt     

product_list = {
        "guitar": 1000, 
        "pick box": 5, 
        "guitar string": 10, 
        "insurance": 5, 
        "priority mail": 10
        }   


shopping_cart = ["guitar", "insurance", "insurance", "priority mail", "priority mail"]

def checkout_2(shopping_cart): 
    
    final_price = 0 
    
    indexes_insurance = [i for i, x in enumerate(shopping_cart) if x == "insurance"]
    
    
    
    indexes_priority = [b for b, y in enumerate(shopping_cart) if y == "priority mail"]
    
    if len(indexes_insurance) > 0: 
        final_price += (product_list["insurance"])
        
    
       
    if len(indexes_priority) > 0: 
        final_price += (product_list["priority mail"])     
        
        
    
    if shopping_cart == []:
        return None
    
    else:
        
        for item in shopping_cart: 
            if item == "insurance":
                continue
            
            elif item == "priority mail": 
                continue
            
            else: 
                final_price += (product_list[item])
            
        
    return final_price

#%% ex. 3
product_list = {
        "guitar": 1000, 
        "pick box": 5, 
        "guitar string": 10, 
        "insurance": 5, 
        "priority mail": 10
        }   


shopping_cart = ["guitar", "insurance", "insurance", "priority mail", "priority mail"]
customer = ["gold", "silver", "normal"]
def checkout_3(shopping_cart, customer): 
    final_price1 = 0 
    
    indexes_insurance = [i for i, x in enumerate(shopping_cart) if x == "insurance"]
    
    
    
    indexes_priority = [b for b, y in enumerate(shopping_cart) if y == "priority mail"]
    
    if len(indexes_insurance) > 0: 
        final_price1 += (product_list["insurance"])
        
    
       
    if len(indexes_priority) > 0: 
        final_price1 += (product_list["priority mail"])     
        
        
    
    if shopping_cart == []:
        return None
    
    else:
        
        for item in shopping_cart: 
            if item == "insurance":
                continue
            
            elif item == "priority mail": 
                continue
            
            else: 
                final_price1 += (product_list[item])
    
    for tier in customer:
            if tier == "gold":
                final_price1 += 0.95 * (product_list[item])
            if tier == "silver":
                final_price1 += 0.98 * (product_list[item])
            if tier == "normal":
                final_price1 += (product_list[item])
            
        
    return final_price1

#you want to create three different tiers of customers:

 #  - normal: No added benefits
  # - silver: 2% discount on products from the ecommerce
  # - gold: 5% discount on everything

 # Modify the checkout function to accept 
 #another parameter with the tier of the 
 #customer and apply the discounts as needed.


























