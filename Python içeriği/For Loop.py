
#for loop

#for loop geçmeden önce incelememiz gereken birkaç tane yardımcı oparatör ve fonksiyon bulunmaktadır.
# Bunlar "in" "not in " ayrıca range() fonksiyonudur.

#in operatörü bir liste içerisinde aranan ifade geçiyorsa True geçmiyorsa False döner.Şunu unutmayalım string ifadelerde
# karakter dizileridir yani bir string ifadeye "in" oparatörünü kullanabiliriz

#not in operatörü ise 'in' operatörünün tam tersi mantıkta çalışır aranan ifade geçmiyorsa True geçiyorsa False döner.

# name = "Mike Tyson"
# print("b" in name)
# print("m" in name)
# print("M" in name)
# #sadece sondaki doğru diğerleri false
# print("M" not in name )
# #derse False çalısır çünkü not in tam tersi


#RANGE fonksiyonu for loop ile sıklıkla kullanılan bir yapıdır.Range fonksiyonun içerisine 100 değerini verirsek
#yani range (100) olursa bize 0'dan 99'a kadar tam sayı listesi döner.

#unutmayın range içerisine herhangi bir argüman verildiğinde verilen argüman "n" kabul edersek "n-1" kadar çalışır
#ayrıca yine aynı senoryada range default olarak sıfırdan başladı.Biz aksini aöyleyemediğimiz sürece range default
# olarak hep sıfırdan başlayacaktır.
"""
for i in range (100):
    print(i)
"""
# #buarada print() fonksiyonu değerleri altalta yazmaktadır.bunu yanyana yazdırmanın yolunu bulun

#range() fonksiyonuna 2 argüman verirsek örneğin 5 ile 10, 5 ten başlayarak 10a kadar bir sayı listesi döner
#range () fonksiyonuna 2 argüman verildiğinde birinci argüman başlangıç değerini ikinci argüman ise bitiş değerini
# temsil eder
"""
for i in range (5,10):
    #print(i)
  """

#range() 3 argüman verirsek 1. argüman başlangıç, ikinci argüman bitiş, üçüncü argüman ise adım miktarını temsil eder
"""
for i in range(1,21,2):
    print(i)
"""

#1-100 arasındaki çift ve tek sayıların toplamını yazdıralım.
"""
tek_toplam=0
cift_toplam=0
for i in range (1,100):       #while loop olduğu gibi adım miktarını biz artırmıyoruz aksini söylemediğimiz sürece 
    if i %2 ==0:               # 1 olarak yani dafult bir kabul edip (adım miktarını) çalışır     
        cift_toplam+=i
    else:
        tek_toplam+=i
        
print(f'{tek_toplam} tek sayıların toplamı' )
print(f'{cift_toplam} çift sayıların toplamı' )
"""

#kullanıcıdan başlangıç bitiş ve adım miktarlarını alalım.Bu şartlara bağlı kalarak her bir adımdaki sayının karesini
# alıp ekrana yazdıralım
#çıktıyı su formatta istiyorum işlemi yaptırarak 25,36 gibi
"""
baslangic= int(input("baslangıc: "))
bitis= int(input("Bitiş: "))
adim_miktar=int(input("adım miktarı: "))

for i in range(baslangic, bitis,adim_miktar):
   kare=i*i
   print(kare)
   
hocanın çözüm yolu:


baslangic= int(input("Başlangıç: "))
bitis= int(input("Bitis: "))
adim= int(input("adim"))
counter=1
for i in range(baslangic,bitis,adim):
    print(f"{counter}.adımda ==> {i**2}")
    counter+=1
"""













