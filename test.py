from ast import Pass
from urllib.parse import ParseResultBytes


import random as rd
for i in range(10):
    if rd.randint(0, 10) in range(5):
        print(1)
    else:
        print(2)