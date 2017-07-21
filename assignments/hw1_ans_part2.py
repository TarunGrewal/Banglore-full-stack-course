def anagram(a,b):
    p=[a]
    a=a.casefold()
    b=b.casefold()
    aa=0
    bw=0
    br=0
    for c in a:
            if  c!= " ":
                bw=bw+1
    for c in b:
            if  c!= " ":
                br=br+1

    for c in a:
        for q in b:
            if(c==q and q!=" "):
                aa=aa+1
                a=a.replace(c,"",1)
                b = b.replace(c, "", 1)


    if(aa==bw and aa==br):
        print("True")
    else:
        print("False")

anagram("abcd","ABCD")
