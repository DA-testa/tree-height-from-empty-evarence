# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    n = int(n)
    level = [0] * n
    count = [0] * n
    lev = []
    c=0
    for i in range(0, n):
        c = 1
        while parents[i] >= 0:
            i = parents[i]
            c=c+1
        lev.append(c)

    
    max_height = 0
    for i in lev:
        if lev[i]>max_height:
            max_height = lev[i]
    return max_height


if __name__ == "__main__":
    mode = input()
    if mode == "I":
        count = int(input())
        text = input() 
  
        text = text.split()
        text = map(int, text)
        text = list(text)

        print(compute_height(count, text))

    elif mode == "F":
        name = input()
        if name.find("a")!=-1:
            return
        with open("./test/" + name, mode="r") as fails:
            count = fails.readline()
            text = fails.readline()
  
        text = text.split()
        text = map(int, text)
        text = list(text)
 
        print(compute_height(count, text))
       
