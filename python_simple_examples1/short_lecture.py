
öğrenciler={
    "deniz":{"notlar":80,"öğrenci_no":1234},
    "ege":{"notlar":60,"öğrenci_no":12345},
    "gizem":{"notlar":67,"öğrenci_no":123456}
    }

print(öğrenciler["deniz"])
print(öğrenciler["deniz"]["notlar"]+5)
print("mert" in "notlar")

#notların ortalamasını ekrana yazdıralım:

notlar=[60,70,80]
t=0

for i in notlar:
    t+=i

ortalama=t/len(notlar)
print("ortalama: ",ortalama)


#2.yol:
notlar=[60,70,80]
t=0

for i in range(len(notlar)):
    t+=notlar[i]
ortalama=t/len(notlar)
print(ortalama)
#notlatı 5 puan arttıralım:

for e in range(len(notlar)):
    notlar[e]+=5
print(notlar)

#2. öğrenci (index 1'deki) hariç hepsinin puanını 5 arttıralım

notlar=[90,72,81,77]

for i in range(len(notlar)):
    if i == 1:
        continue
    notlar[i]+=5
print(notlar)

#listenin içinde belirli bir eleman var mı diye kontrol edelim:

x=int(input(("hangi sayıyı kontrol edelim: ")))

l=[100,200,30,40]

for i in l:
    print(i) #iterasyon break ile çıkmış mı görelim mi diye...
    if x==i:
        print("buldummm..")
        break

#DİCTİONARY'LERDE İTERASYON:

#defult olarak elemanlarında dolaş deyince "key"lerde iterasyon yapılıyor
#değerlerine ulaşmak istiyorsam şu şekilde yapılıyor:

d={"student_1":[80,60],"student_2":[50,75]}
for k in d:
    v=d[k]
    print(v)

#veya d.values diyerek value'larında iterasyon yapalım.
d={"student_1":80,"student_2":50}

for v in d.values():
    print(v)

#75'den fazla alan bir öğrenci var mı diye kontrol etmek istiyorum:

for k in d:
    value=d[k]
    if value >75:
        print(k)

#birden çok değişkeni bie seferde eşitleyelim:

for k,v in d.items():
    print("key değeri:", k,"value değeri:", v)