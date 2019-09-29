import datetime


a = input('Дата (дд-мм-гггг): ')
a = a.split('.')
aa = datetime.date(int(a[2]), int(a[1]), int(a[0]))
bb = datetime.date.today()
cc = (bb-aa) // 365
print(str(cc).split()[0])