
def j():
    f=input("Enter No ")
    f=int(f)
    if(f>0):
        while(f>=0):
            print(f,end=" ")
            f=f-1
    elif(f<0):
        while (f <= 0):
            print(f)
            f = f + 1
    print("")
j()
