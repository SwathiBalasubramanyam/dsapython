#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaxFun' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY singer
#  2. INTEGER_ARRAY length
#

def getMaxFun(singer, length):
    # Write your code here

    zipped_singers = list(zip(singer, length))
    max_fun = 0
    for i in range(len(singer)):

        singers = set()
        fun = 0
        
        for item in zipped_singers[i:length-i]:
            s, l = item
            singers.add(s)
            fun += len(singers) * l
        max_fun = max(max_fun, fun)
    return max_fun
        
