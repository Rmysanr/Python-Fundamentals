#DÖNGÜLERRR

"""
#0-100 ARASINDAKİ SAYILARI YAZIDRALIM.LOOPLARDA SAYAC MANTIĞI VAR.AŞAĞIDAKİ ÇÖZÜM HOCANIN.(DERS)
sayac=0
while <=100:
    print(sayac)
    sayac+=1

"""

#Soru:1-101 arasında kaç tane çift kaç tane tek sayı var ayrı ayrı bulalım
"""
sayac_cift=0
sayac_tek=0
a=1
while  a <=101:
    if a%2==0:
        sayac_cift+=1
        a+=1
    else:
        sayac_tek+=1
        a+=1
print(sayac_cift)
print(sayac_tek)
"""

#Soru: 1 ile 100 arasındaki çift ve tek sayıların ayrı ayrı toplamlarını yazdıralım
"""

cift_toplam=0
tek_toplam=0
sayac=1
while sayac<=101:
    if sayac %2==0:
        cift_toplam+=sayac
        sayac+=1
    else:
        tek_toplam+=sayac
        sayac+=1
print(tek_toplam)
print(cift_toplam)
"""

#Soru: 1 ile 101 ARASINDAKİ TEK VE ÇİFT SAYILARIN MİKTARINI YAZAN UYGULAMA YAPALIM (DERS)
"""
cift_miktar=0
tek_miktar=0
sayac=1     #SAYAC 1 ÇÜNKÜ SORUDA 1-101 ARASINDAKİ SAYILAR İSTENMİŞ SAYAC BU ARALIKTAKİ SAYILARI TEK TEK ZİYARET EDECEK

while sayac<= 100:
    if sayac %2 ==0:
        cift_miktar+=1

    else:
        tek_miktar+=1
    sayac+=1
print(f' {cift_miktar} tane çift sayı vardır' )
print(f'{tek_miktar} tane tek miktar vardır ')
"""
"""
#1-1000 arasındaki çift ve tek sayıların toplamlarını yazdıralım(HOCA-DERS)

cift_toplam=0
tek_toplam=0
sayac=1            #SAYACIN İF BLOKLARINDAN AYRI ARTMASINI İSTİYORUM.BAĞIMSIZ OLARAK ARTSIN.HER İKİ BLOKTA
                   #GEREKMİYOR. WHİLEN ALTINDA İF VE ELSE BLOKLARI İLE AYNI HİZADA SAYACI ARTIRMALISIN!!(DERS)

while sayac<=1000:
    if sayac %2==0:
        cift_toplam+=sayac
    else:
        tek_toplam+=sayac

    sayac+=1

print(tek_toplam)
print(cift_toplam)







#Soru: Kullanıcıdan bir işlem sembolü alalım (+,- vb).Bu seçilen işlem sembolü üzerinden kullanıcının girdiği 2 sayı
# ile aritmatiksel işlem yapalım.Kullanıcı işlem sembolü seçmek yerine "e " harfi girerse uygulama dursun.
# Kullanıcı isteği kadar işlem yapabilsin
"""
"""
while True:
    sayi_1= int(input("Bir sayı giriniz: "))
    sayi_2= int(input("Bir sayı giriniz: "))
    islem = input(" lütfen bir islem giriniz: ")

    if islem == "+" :
        print(sayi_1 + sayi_2)

    elif islem == "-" :
        print(sayi_1 - sayi_2)

    elif islem == "*":
        print(sayi_1 * sayi_2)

    elif islem == "/":
        print(sayi_1 / sayi_2)

    elif islem == "e":
        break

    else:
        print("Doğru işlem giriniz")
"""
"""
#DAHA KISA YOLU AYNI İŞLEM AMA KISA YOLU (DERS)

while True:
    
    prosess=input("İşlem türü giriniz: ")

    if prosess == "e":
        print("Uygulama kapatılıyor...")
        break
    else:
        sayi_1 = input("sayi=")
        sayi_2= input("sayi2: ")

        if prosess "+":
            print(f'Sonuç: {sayi_1+sayi_2}')
        elif prosess "-":
            print(f'Sonuç: {sayi_1 - sayi_2}')
        elif prosess "*":
            print(f'Sonuç: {sayi_1 * sayi_2}')
        elif prosess "/":
            print(f'Sonuç: {sayi_1 / sayi_2}')
        else:
            print(f'Doğru işlem bilgisi giriniz')
"""






"""
#1-101 arasındaki tek sayıların toplamı

sayac=1
toplam=0
while sayac<102:
    if sayac%2!=0:
        toplam=toplam+sayac
    sayac+=1
print(toplam)
"""
"""
# İN OPARETÖRÜ İLE BİR LİSTE İÇERİSİNDE İTEM VARSA TRUE YOKSA FALSE DÖNER.
# YANİ BURADA KULLANICININ GİRSİĞİ İŞLEM BİZİM İŞLEM TÜRÜ LİSTENİZDE
# VARSA tRUE YOKSA FALSE DÖNECEK (HOCAA)

prosess_type_list=['+', '-', '*', '/','e']

while True:
    prosess=input("İşlem türü giriniz: ")
    if prosess in prosess_type_list: 
        if prosess =='e':
            print('Uygulama kapatılıyor..')
        else:
            sayi_1 = input("sayi=")
            sayi_2 = input("sayi2: ")

            if prosess "+":
                print(f'Sonuç: {sayi_1 + sayi_2}')
            elif prosess "-":
                print(f'Sonuç: {sayi_1 - sayi_2}')
            elif prosess "*":
                print(f'Sonuç: {sayi_1 * sayi_2}')
            elif prosess "/":
                print(f'Sonuç: {sayi_1 / sayi_2}')
    else:
        print("Doğru işlem giriniz")

"""

#1950 yılı ile günümüz arasındaki  kullanıcıdan bir yıl bilgisi alalım şayet 1950 ve günümüz arasında ise "Buldunuz"
# Değilse bulamadık diye feedback veren uygulama yaz
"""
yil=int(input("Lütfen yıl bilgisi giriniz: "))
if 1950<=yil<=2023:
  print("Buldunuz")
else:
  print("Bulamadık")
"""

#KULLANICIDAN YIL BİLGİSİ ALACAĞIZ BU YIL BİLGİSİ 1943 DEĞİLSE ARADIĞINIZ YIL BULUNAMMAKTADIR UYGULAMASI YAZIN(DERS)
#ÖNEMLİ!!

"""
from datetime import datetime 

started_date =1943
search_date =int (input("aradığınız yılı girin: "))
is_exist=False

while started_date <= datetime.now().year:    #baştakini yapabilmek için bunu yazdık günümüz yılını 2023 olarak değilde 
    if started_date == search_date:           #now olarak yazdık
        print("Buldunuz")
        is_exist = True
        break

    started_date+=1

if not is_exist:  # true değilse demek tani false ise yıkardaki gibi yukarda biz değişkene true yaptık.Tutmadığı zamanlarda
    print("Aradınığınız tarih bulunamadı...")
        
BENİMKİ;

yil=int(input("yıl: "))
sayac=1943

while sayac<=2023:
    if yil==sayac:
        print("Buldunuz")
        break
    sayac+=1

if not is_exist:
    print("BulUnamadı")

"""

#0-101 arası tek sayıların toplamını bul continue kullanarak
"""
sayac=0
toplam=0

while sayac<= 101:
    sayac += 1
    if sayac %2 == 0:
        continue
    else:
        toplam+=sayac

print(toplam) 

"""


#Kullanıcıdan başlangıç bitiş ve adım miktarları alarak bir loop kuralım.
# Kullanıcının istediği adım miktarına göre sayıları toplatarak ekrana yazdıralım. HATAAAA

"""
baslangic= int(input("Başlangıc= "))
bitis= int (input("Bitiş:"))
adim = int (input( "adım miktarı: "))
toplam=0

while baslangic<bitis:
    baslangic=baslangic+adim
    toplam=baslangic+baslangic+adim
print(toplam)
"""
#Sayı tahmin oyunu 1-100 arasında rastgele bir sayı üretildiğini düşünelim.Kullanıcı bu üretilen sayıyı 3 hakta tahmin
# etmeye çalışacak.Kullanıcı üretilen sayıdan daha büyük  bir sayı girerse daha küçük bir sayı giriniz ya da üretilen
# sayıdan daha büyük sayı giriniz şeklinde yönlendireceğiz #HAAAATAAA

"""
uretilen_sayi=int(input("üretilen sayi= "))
if 1<= uretilen_sayi<=100:
    hak = 3
    while hak > 0:
        tahmin_sayi = int(input("kullanıcının girdiği sayi= "))
        if tahmin_sayi > uretilen_sayi:
            print("Daha küçük sayı giriniz")
        elif tahmin_sayi < uretilen_sayi:
            print("Daha büyük bir sayı giriniz")
        elif tahmin_sayi== uretilen_sayi:
            print("Buldunuz")
            break
        hak -= 1
    else:
        print("bulamadınız")
else:
    print("aralıkta seçiniz")
"""

#Kullanıcıdan alınan sayının asal olup olmadığını ekrana yazdıralım
"""
sayi = int(input("Bir sayı giriniz: "))
if 1<sayi:
    bolen = 2
    if sayi == bolen:
        print("Asaldır")
    else:
        while sayi % bolen != 0:
            bolen += 1
            if bolen == sayi:
                print("asaldır")
                break
        else:
            print("Asal değildir")
else:
    print("asal değildir")
"""







































