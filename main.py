# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import random

def getPower():
    print("")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("+      this modular for caculate power!    +")
    print("+      designed by rengrongfeng            +")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    atp = input("ATP:")
    adp = input("ADP:")
    pi = input("Pi:")
    r = input("R:")
    t = input("T:")
    de = input("detaG0:")
    g = float(de) + float(r) * math.log(float(adp) * float(pi) / float(atp))
    return g


def getRandomBasicGroup(count):
    print("")
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("+      this modular for random basic group!   +")
    print("+      designed by rengrongfeng               +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    basicGroup="ATGC"
    Sequence=""
    for i in range(int(count)):
        index = random.randint(0,3)
        Sequence = Sequence + basicGroup[index]
    return Sequence

def writeFileTest():
    print("")
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("+      this modular for random basic group!   +")
    print("+      designed by rengrongfeng               +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++")




def main():
    print("")
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("+       number 1 is get power                 +")
    print("+       number 2 is get random basic group    +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    function = input("please select function(1-2):")
    string = "funtion number erro"
    if int(function) == 1:
        string = getPower()
    if int(function) == 2:
        string = getRandomBasicGroup(input("count:"))
    print(string)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
