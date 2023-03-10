# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
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
 
    #print(max_height)
    return max_height


def main():
    mode = input()
    if "I" in mode:
        count = int(input())
        text = input() 
  
        text = text.split()
        text = map(int, text)
        text = list(text)

        print(compute_height(count, text))

    elif "F" in mode:
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
       

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
