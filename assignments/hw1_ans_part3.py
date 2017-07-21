def is_permutation(y):
    a=0
    for i in range (1,len(y)+1):
        for p in range(0,len(y)):
            if(i==y[p] and y.count(i)<=1):
                a=a+1
    if(len(y)==a):
        return True
    else:
        return False
print(is_permutation([2,1,3]))
