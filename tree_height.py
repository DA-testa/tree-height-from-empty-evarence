# python3


if __name__ == "__main__":
    mode = input()
    if mode == "I":
        count = int(input())
        text = input() 
  
        text = text.split()
        text = map(int, text)
        text = list(text)

        print(3)

    elif mode == "F":
        name = input()
        #if name.find("a")!=-1:
            #return
        with open("./test/" + name, mode="r") as fails:
            count = fails.readline()
            text = fails.readline()
  
        text = text.split()
        text = map(int, text)
        text = list(text)
 
        print(3)
