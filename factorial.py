# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 04:57:06 2022

@author: User
"""

import sys

data1 = sys.argv[1]
data2 = sys.argv[2]
def hello_world(x):
    if x == 1:
        return 1
    else:
        return x * hello_world(x - 1)
def hello_world2(x):
    if x == 1:
        return 1
    else:
        return x * hello_world2(x - 1)    

print(hello_world(int(data1)))
print(hello_world2(int(data2)))
