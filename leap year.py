Task 
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird



#!/bin/python3

import math
import os
import random
import re
import sys


v
if __name__ == '__main__':
    n = int(input().strip())
if(n%2==1):
 print("Weird")
elif(n in range(2,6)):
 print("Not Weird") 
elif(n in range(6,21)):
 print("Weird") 
else: 
    print("Not Weird")
