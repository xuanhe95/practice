f=open('/Users/zhang/Documents/GitHub/practice/IntegerArray.txt','r')
lines=f.read().splitlines()
lst=[]
for i in lines:
    lst.append(int(i))

def inversion(lst):
    if len(lst)==1:
        return lst,0
    p=len(lst)//2

    left,count_left=inversion(lst[:p])
    right,count_right=inversion(lst[p:])

    combined,count=merge_and_count(left,right)
    return combined,count+count_left+count_right

def merge_and_count(x,y):
    combined=[]
    count=0
    while len(x) and len(y):
        if x[0]>y[0]:
            combined.append(y.pop(0))
            count+=len(x)
        else:
            combined.append(x.pop(0))
    return combined+x+y,count


print(inversion(lst))