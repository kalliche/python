def edad_calculadora(y,m,d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    age = int((today-dob).days/365.25)
    print(age)
edad_calculadora(1986,10,31)