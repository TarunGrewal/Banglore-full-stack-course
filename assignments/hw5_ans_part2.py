class reg():
    def count_all_enrolled_students(self,re):
        self.re=re
        t=[]
        for i in re.keys():
            t.extend(re.get(i))
        u=set(t)
        print("1. ",len(u),"students")



    def find_invalid_registration(self,d,f,g):
        self.d=d
        self.f=f
        self.g=g
        for i in d:
            p=d.get(i)
            for j in f:
                if(i==j):
                    o=f.get(j)
                    k=g.get(o)
                    print("2. ",i,":",o,":->",list(set(p).difference(set(k))))
    def notify_exam_conflict(self,w,course_codes):
        l=[]
        self.w=w
        ll=[]

        self.course_codes=course_codes

        for i in course_codes:
            l.extend(w.get(i))
        for j in l:
            if(j not in ll):
                ll.append(j)

        r = []
        for i in l:
            if i in ll:
                ll.remove(i)
            else:
                r.append(i)
        print("3.",r,"have an exam time conflict")
    def hold_workshop(self,s):
        self.s=s
        r=[]
        for i in s:
            if(i!="Python_101"):
                r.extend(d.get(i))
        t=set(r)
        print("4.",t," are not attending Python 101 course")


d = {}
d["Python_101"] = ["Helen", "Jesus", "Menna","Martin"]
d["Data_sc"] = ["Ojas", "Martin", "Eli","Menna"]
d["Fintech"] = ["Ojas", "Jesus", "Martin", "Eli"]
f={
    "Python_101":"Lab1",
    "Fintech":'Lab2'}
g={
    "Lab1":["Helen","Menna"],
    "Lab2":["Martin","Eli"]}
tim={
    "Python_101":"8:00 A.M",
    "Data_sc":"8:00 A.M",
    "Fintech":"9:00 A.M"}
v=[]
for p in tim:
    for q in tim:
        if(p!=q and tim.get(p)==tim.get(q) and tim.get(p) not in v):
            v.append(p)



r=reg()
r.count_all_enrolled_students(d)
r.find_invalid_registration(d,f,g)
r.notify_exam_conflict(d,v)
r.hold_workshop(d)
