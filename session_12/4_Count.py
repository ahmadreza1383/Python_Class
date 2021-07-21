#///////////////////// از کانت برای گرفتن تعداد کاراکتر استفاده میکنیم
v = {'a' : 0 ,'e' : 0 ,'i' : 0 ,'o' : 0 ,'u' : 0 }

sentence = input('inter sentence : ')
for i , j in v.items():
    j = sentence.count(i)
    print(i , j)
