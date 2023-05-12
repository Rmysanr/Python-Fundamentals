"""
n=int(input("sayı: "))
if n % 2==0 and n>20:
    print("not weird")
elif n % 2 == 0 and n in range (2,5):
    print("not weird")
elif n % 2 == 0 and n in range (6,21):
    print("weird")
else:
    print("weird")
"""
#ÇARPIM TABLOSU:
"""
for i in range(1,10):
    print("*************")
    for j in range(1,10):
        print("{} x {} = {}".format(i,j,i*j))

"""
#KULLANICIDAN ALDIĞIMIZ BİR SAYININ MÜKEMMEL BİR SAYI OLUP OLMADIĞINI BULUNUZ:

"""
sayı=int(input("sayı: "))
i=1
toplam=0
while (i < sayı):
    if(sayı % i ==0):
        toplam +=i
    i+=1
if (toplam == sayı):
    print("sayınız mükemmel sayıdır.")
else:
    print("sayınız mükemmel sayı değildir.")
"""
#FAKTÖRİYEL BULMA PROGRAMI:
#ÇIKMAK İÇİN "q" BASIN:
"""
while True:
    sayı=int(input("sayı: "))
    if(sayı=="q"):
        print("program sonlandırıldı...!")
        break
    else:
        sayı=int(sayı)
        faktöriyel=1
        for i in range(2,sayı+1):
            faktöriyel*=i
            print("i:",i,"faktöriyel:",faktöriyel)
    print("faktöriyel: ",faktöriyel)

"""