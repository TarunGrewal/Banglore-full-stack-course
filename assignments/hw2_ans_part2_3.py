from datetime import  datetime, timedelta


def mul(bday1, bday2):

    bday1 = datetime.strptime(bday1,"%d/%m/%Y")
    bday2 = datetime.strptime(bday2, "%d/%m/%Y")
    person1 = datetime.date(bday1)
    person2 = datetime.date(bday2)

    a = (person2 - person1)

    p1 = int(a.days)
    d = person2 + timedelta(days=p2)
    print("Date at twice age:", d))
mul("30/12/1990", "31/12/2000")
