
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 03:15:00 2019

@author: vishu
"""


#linear search

def linearsearch(a,n):
    for i in a:
        if i==n:
             print("found at index:",a.index(i))


a=list(map(int,input().split()))
print(a)
n=int(input())
linearsearch(a,n)
       
