def a():
    friends={}
    friends["Lesley"] = ["Helen", "Jesus", "Menna"]
    friends["Jacob"] = ["Ojas", "Martin", "Eli"]
    friends["Shreyas"] = ["Ojas", "Jesus", "Martin", "Eli"]
    friends["Ojas"] = ["Jacob", "Shreyas", "Jesus"]
    friends["Jesus"] = ["Lesley", "Eli", "Keala"]
    n=list(friends.keys())
    z=[]
    zz=[]
    for i in range(len(friends)):
        h=list(friends.keys())[i]
        h=str(h)
        for j in range(0,len(friends.get(h))):
            m=str(list(friends.get(h))[j])
            for p in range (len(friends)):
                mm=str(list(friends.keys())[p])
                if(m==mm):
                    for p in range (len(friends.get(mm))):
                        k=str(list(friends.get(mm))[p])
                        if(k not in friends.get(h) and k!=h and k not in z):
                            z.append(k)
        zz.append(z)
        z=[]
    d=list(zip(n, zz))
    for u in range (0,len(d)):
        print(d[u])
a()
