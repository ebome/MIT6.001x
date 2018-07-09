# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:27:16 2018

@author: Alisa
"""

s = 'oboboboboboboboobobooojoboobobo'
count=0
num=0
while num < len(s)-2:
    if s[num]=='b' and s[num+1]=='o' and s[num+2]=='b':
        count+=1  
    num+=1

print("Number of times bob occurs is: "+str(count))