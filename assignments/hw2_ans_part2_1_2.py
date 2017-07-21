import datetime
import time
def p(d,m,y):
    q=datetime.date.today()
    a=time.strftime('%X')
    asplit = a.split(':')
    print(datetime.date.today())
    print(datetime.datetime.now().strftime("%A"))
    print(time.ctime())
    if q.month < m or q.month ==m and q.day <d:
        print("Current age:",datetime.date.today().year-y)
    if q.month < m or q.month == m and q.day < d:
        print(m-q.month,"months",d-q.day-1,"days",int(24-float(asplit[0])),"hours",int(60-float(asplit[1])),"minutes",int(60-float(asplit[2])),"seconds left in next birthday")
p(16,12,1997)
