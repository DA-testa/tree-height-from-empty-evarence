# python3

import sys
import threading


def compute_height(n, parents):
    lev = [-1] * n
    
    def max_height(x): 
        if x == (-1):
            return -1  
        
        if lev[x] == (-1):
            lev[x] = 1 + max_height(parents[x])
        return lev[x]    

    for x in range(n):
        max_height(x)
    return max(lev) +1


def main():
    mode = input()
    if mode == "I":
        n = int(input())
        text = input()
        text = text.split()
        parents = (list(map(int, text)))
        print(compute_height(n, parents))

    elif mode == "F":
        name = input()
        if name.find("a")!=-1:
            return
        with open("./test/" + name, mode="r") as fails:
            count = fails.readline()
            text = fails.readline()
            parents = (list(map(int, text.split())))
            print(compute_height(count, text))
       
main()
    
