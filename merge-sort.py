def MergeSort(lst, p,r):
    if(p >=r):
        return
    q= (p+r)//2
    MergeSort(lst,p, q)
    MergeSort(lst,q+1,r)
    Merge(lst,p,q,r)

def Merge(lst,p,q,r):
    leftLstLength = q-p+1
    rightLstLength = r-q
    leftLst = [0]*(leftLstLength)
    rightLst = [0]*(rightLstLength)
    for i in range(0,leftLstLength):
        leftLst[i] = lst[p+i]
    for j in range(0, rightLstLength):
        rightLst[j] = lst[q+j+1]
    i=0
    j=0
    k=p
    while(i < leftLstLength and j < rightLstLength):
        if(leftLst[i] < rightLst[j]):
            lst[k] = leftLst[i]
            i= i+1
        else:
            lst[k]= rightLst[j]
            j=j+1
        k= k+1
    while(i < leftLstLength):
        lst[k] = leftLst[i]
        i=i+1
        k=k+1
    while(j < rightLstLength):
        lst[k] = rightLst[j]
        j=j+1
        k=k+1

lst = [2,1,4,3,34,45,0,12,34]
MergeSort(lst,0,len(lst)-1)
print(lst)