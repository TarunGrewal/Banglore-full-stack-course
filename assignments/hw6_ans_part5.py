
import math
def lists():
    comprehension=[]
    for i in range(1,11):
        comprehension.append(int(math.pow(i,3)))
    print(comprehension)
def vov(s):
    vowels=['a','e','i','o','u']
    s.lower()
    p=[]
    for i in vowels:
        if i in s and i not in p:
            p.append(i)
    print(p)

lists()
vov("tarun")
def g():
    p=0
    [x + y for x in [10, 20, 30] for y in [1, 2, 3]]
    for x in [10,20,30]:
        for y in [1,2,3]:            
            print(x+y,end=" ")
    print()
g()
