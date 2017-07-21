def prime():
    k=input("Enter Number ")
    k=int(k)
    p=True
    for i in range (2,k):
        if(k%i==0):
            p=False
            break
    if(p==True):
        print("It is prime")
    else:
        print("it is not prime")
prime()

