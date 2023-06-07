
# ENUMERATE_ZIP:

adlar=['tyler','blakE','cory','cameron']

for i,e in enumerate(adlar):
    print(i,'indexsindeki eleman:',e)

#ZIP:

öğrenciler=['öğrenci_1','öğrenci_2','öğrenci_3']
notlar=[70,80,90]

#1.yol:

for i in range(len(öğrenciler)):
    s=öğrenciler[i]
    g=notlar[i]
    print(s,g)
#2.yol:

for s,g in zip(öğrenciler,notlar):
    print(s,g)

#3.yol:

for e in zip(öğrenciler,notlar):
    print(e)

#4.yol:

for i in range(len(öğrenciler)):
    print(öğrenciler[i],notlar[i])

#her ayki karı hesaplama:

satis=[3500.00,76300.00,67200.00]
maliyet=[56700,21900.00,121000.00]

#1. yol
for i in range(len(maliyet)):
    s=satis[i]
    m=maliyet[i]
    kar=s-m
    print(f'total profit:{kar}')
#2.yol:

for s,c in zip(satis,maliyet):
    kar=s-c
    print(f'total prifit: {kar}')


#zip() ile dictionary yaratmak:

keys=['isim','soyad','ulke','is']
values=['deniz','walker','turkey','data scientist']

d={}
for k,v in zip(keys,values):
    d[k]=v
print(d)