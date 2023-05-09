#karar mekanizması (if -elif-else)

#if kullanımı:
"""
if şart cümlesi :
    kod bloğu
else:    else şart cümlesi içermez çünkü if bloğunda verilen şart tutmama durumunu kontrol eder
    kod bloğu
"""

#region example -1
"""
sayi_1 = int(input("Sayı Giriniz: "))
sayi_2 = int(input("Sayı Giriniz: "))

if sayi_1 > sayi_2:
    print(f' {sayi_1} büyüktür ')
else:
    print(f' {sayi_2} büyüktür')
"""
#endregion

#region example -2

#kullanıcıdan alınan bir sayı tek i çift mi
"""
sayi = int(input("Bir sayı giriniz: "))

if sayi % 2 == 0:
    print( f' {sayi } çifttir')
else:
    print(f' {sayi} tektir')
"""
#endregion

#region example -3

#kullanıcıdan alınan sayı pozitif mi negatif mi nötr mü?
"""
sayi=int(input("Bir sayı giriniz: "))

if sayi < 0:
    print(f' {sayi } negatiftir')
elif sayi==0:
    print(f' {sayi} nötrdür')
else:
    print(f' {sayi} pozitiftir')
"""




