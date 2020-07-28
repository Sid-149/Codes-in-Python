#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

str1=''
for i in range(m):
    for j in range(n):
        str1=str1+matrix[j][i]

str1=re.sub(r'\b[^a-zA-Z0-9]+\b',r' ',str1)
print(str1)
