import math
def prim(num):
    if(num == 0):
        return -1
    if(num <0):
        num=num*-1
    if(num < 4):
        return True
    gyok = math.sqrt(num)
    i=4
    while(i<gyok):
        if (int(gyok) % i == 0):
            return False
        i+=i
    return True
print prim(0)
