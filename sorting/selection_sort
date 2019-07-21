#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:43:27 2019

@author: vishant
"""

def selection(a):
    for j in range(len(a)):#scanning element
        min=j;
        for k in range(j+1,len(a)): # checking min element from list
            if a[min]> a[k]:
                min=k
        a[j],a[min]=a[min],a[j]
                


a=list(map(int,input().split()))
print("unsorted:",a)   
selection(a) 
print("sorted:",a)    
