def fibonacci():
    num=input("Enter Number ")
    num=int(num)
    c=-1
    v=1
    f=c+v
    while(f<num):
        print(f,end=" ")
        c=v
        v=f
        f=c+v
print("")
fibonacci()
