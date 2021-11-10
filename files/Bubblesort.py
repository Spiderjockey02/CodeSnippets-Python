def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [36,38,30,31,38,43,55,38,37,30,48,41,33,25,34,43,37,40,36]
bubbleSort(alist)
print(alist)
