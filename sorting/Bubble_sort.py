#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:43:27 2019

@author: vishant
"""

def bubble(a):
  for i in range(len(a)-1):
      for j in range(i+1,len(a)):
          if a[i]>a[j]:
              a[j],a[i]=a[i],a[j]
                 
a=list(map(int,input().split()))
print("unsorted:",a)   
selection(a) 
print("sorted:",a)    
