
#girilen 3 basamaklı bir sayının basamaklarının küpleri toplamı sayının kendisine eşit olup olmadığını bulan program kod:
toplam=0
liste=[]
sayi=input("sayı: ")
if len(sayi)!=3:
    print("yanlış")
else:
    for i in sayi:
        liste.append(i)
        toplam+=int(i)**3
    if toplam==int(sayi):

        print("toplamınız{} sayınıza{} eşittir...".format(sayi,toplam))
    else:
        print("toplamınız{} sayınıza{} eşit değildir".format(sayi,toplam))

import math

#klavyeden girilen 20 adet sayıdan çift sayıların toplamını tek sayıların toplamının oranını bulan uygulamayı yapınız.

çift_toplam=0
tek_toplam=0
sayac=20

while sayac>0:
        sayı=int(input("lütfen sayı giriniz: "))
        if sayı % 2 == 0:
            çift_toplam+=sayı
        if sayı %2 != 0:
            tek_toplam += sayı
        sayac -=1
print(f'{çift_toplam}/{tek_toplam}')

#10 ile 1000 arasında ki tam kare sayıları ekrana yazdıran program yazınız:

list=[]
list2=[]
for i in range(10,1000):
    if i**2 in range(10,1000):
        list2.append(i**2)
print(list2)



