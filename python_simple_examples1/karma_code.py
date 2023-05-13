#bir cümle içerisinde geçen sesli harflerin bulan kod yazınız:
"""
cümle=input("bir cümle giriniz: ")
sesli_harfler="aeıioöuü"

for i in cümle:
    if i in sesli_harfler:
        print(i,end=',')
"""
#bir cümle içerisinde geçen harfin kaç defa geçtiğini bulunuz:
"""
cümle=input("bir cümle giriniz: ")
sayaç=0
harf="a"

for i in cümle:
    if i == "a":
        sayaç+=1
print("cümle içerisindeki a harfinin sayısı: ",sayaç)
"""
#kullanıcı tarafından girilen bir karakter dizisi içerisinde geçen sesli ve sessiz harfleri ayrı ayrı listelere atayan program yazınız.,
"""
sesli_harfler="aeıioöuü"
sessiz_harfler="bcçdfgğhjklmnprsştvyz"
cümle=input("bir cümle giriniz: ")
sesliler=[]
sessizler=[]
for i in cümle:
    if i in sessiz_harfler:
        sessizler.append(i)
for j in cümle:
    if j in sesli_harfler:
        sesliler.append(j)
print("sesli harfler: ",sesliler,end=' ')
print("sessiz harfler: ",sessizler,end=' ')
"""
#kullanıcıdan sinema ya da tiyatro tercihi sorulsun. sinema izlemek için 15tl, tiyatro izlemek için 10 tl ödemesi gerekmektedir.
#öğrencilere %50 indirim yapıldığı düşünülerek öğrenci ise indirim yapılan;öğrenci değil ise indirimsiz tutarını hesaplayarak ekrana yazdıran kod:
"""
secim=input("sinema için(1),tiyatro için(2) tuşlayınız...")
öğrenci=input(("öğrenci misiniz?(E\H): "))
tutar=0

#öğrenci değil:
if secim=='1':
    tutar+=15
elif secim=='2':
    tutar+=10
#öğrenci İNDİRİMİ:

if öğrenci=='E' or öğrenci=='e':
    tutar=tutar/2

print("ödemeniz gereken tutar: ",format(tutar))
"""