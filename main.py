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
    data = []
    for line in open('D:\data.txt'):
        length = float(line.strip())
        data.append(length)
    n_items = len(data)
    total = sum(data)
    shortest = min(data)
    longest = max(data)
    data.sort()
    output = open("D:\results.txt","w")
    output.write("number of dendritic length:%4i \n" %(n_items))
    output.write("total dendritic length    :%6.1f \n" %(total))
    output.write("shortest dendritic length :%7.2f \n" %(shortest))
    output.write("longest dendritic length  :%7.2f \n" %(longest))
    output.write("%7.2f \n %7.2f" %(data[-2],data[-3]))
    output.close()



def main():
    print("")
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("+       number 1 is get power                 +")
    print("+       number 2 is get random basic group    +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    function = input("please select function(1-3):")
    string = "funtion number erro"
    if int(function) == 1:
        string = getPower()
    if int(function) == 2:
        string = getRandomBasicGroup(input("count:"))
    if int(function) == 3:
        writeFileTest()
        string = "fuction 3 is done"
    print(string)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
