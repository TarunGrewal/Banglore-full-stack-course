class luhn(object):
    dct0=""
    def determine_card_type(self,dct):
        a=str(dct)
        self.dct=a
        if(a[0]=="4"):
            luhn.dct0="Visa"
            return (luhn.dct0)
        elif(a[0]=="5" and (a[1]=="1" or a[1]=="2" or a[1]=="3" or a[1]=="4" or a[1]=="5")):
            luhn.dct0="Mastercard"
            return (luhn.dct0)
        elif(a[0]=="3" and (a[1]=="4" or a[1]=="7")):
            luhn.dct0="Apex"
            return (luhn.dct0)
        elif(a[0:4]=="6011"):
            luhn.dct0="Discover"
            return (luhn.dct0)
        else:
            return False
    def check_len(self,v):
        self.v=v


        if(len(v)==16 or len(v)==15):
            return True
    def valid(self,c):
        self.c=c
        k = []
        p = 0
        h = ""
        for j in range(0, len(c)):
            k.append(c[j])
        k.reverse()
        for i in range(1, len(k), 2):
            k[i] = str(int(k[i]) * 2)
        for m in range(0, len(k)):
            h = h + k[m]
        for mm in range(0, len(h)):
            p = p + int(h[mm])
        if (p % 10 == 0):
            return True
        else:
            return False

q=luhn()
qq=input("Enter number ")
q.determine_card_type(qq)
if(q.determine_card_type(qq)!=False):
    if(q.check_len(qq)==True):
        if(q.valid(qq)==True):

            print(q.determine_card_type(qq))
        else:
            print("Not Valid")
    else:
        print("Not Valid")
else:
    print("Not Valid")

