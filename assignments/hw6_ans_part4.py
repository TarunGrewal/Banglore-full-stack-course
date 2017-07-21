import cmath
a = input("1st ")
b = input("2nd " )
c = input("3rd ")
a=int(a)
b=int(b)
c=int(c)
d = (b**2) - (4*a*c)
if(d==0):
    print("Real and double root :",d/2*a)
elif(d>0):

    s1 = (-(b+cmath.sqrt(d)))/(2*a)
    s2 = (-(b-cmath.sqrt(d)))/(2*a)
    print("Real Roots",s1,s2)
elif(d<0):
    print("Error! Roots are Complex")
