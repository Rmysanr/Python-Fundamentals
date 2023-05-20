#code1:

#aşağıdaki sözlükleri oluşturarak sizlerden istenen işlemleri yapınız:
sozluk={"bilim insanı":"aziz sancar",
        "şair":"mehmet akif ersoy",
        "astronom":"ali kuşçu"

        }
#a)sozluk isimli sözlüğü meslekler isimli başka bir sözlüğe kopyalayınız ve yazdırınız...

meslek=sozluk.copy()
print(meslek)

#b)sozluk isimli sözlüğün değerlerini ekrana yazdıralım:

print(sozluk.values())

#c)sozluk isimli sözlüğün içi boş bir sözlük haline getirelim:

sozluk.clear()
print(sozluk)

#ç)sozlük isimli sözlüğe Matematikçi:Cahit Arf ikilisini ekleyelim:

sozluk["matematikçi"]="Cahit Arf"
print(sozluk)

#d)sozluk isimli sözlüğün içinde sanatçı anahtarının olup olmadığını sorgulayın:

print(sozluk.get("sanatçı"))

#e)sozlük isimli sözlüğün bilim insanı anahtarındaki değeri Canan Dağdeviren olaran değitirin:

sozluk["bilim insanı"]="Canan Dağdeviren"
print(sozluk)

#f)sozluk isimli sözlüğün şair anahtarı ile eşleşen değeri ekrana yazdırın:

print(sozluk["şair"])

#code2:

onemli_bilgiler={"acil çağrı merkezi":"112",
                 "polis imdat":"155",
                 "milli eğitim bakanlığı iletişim merkezi":"444 0 632"
                 }

#a)önemli_bilgiler isimli sözlüğün değerlerini ekrana yazdıralım:

print(onemli_bilgiler.values())

#b)önemli_bilgiler isimli sözlüğü siliniz:

onemli_bilgiler.clear()
print(onemli_bilgiler)

#c)önmeli_bilgiler isimli sözlükte acil çağrı merkezi anahtarını ve değerini siliniz:

onemli_bilgiler.pop("acil çağrı merkezi")
print(onemli_bilgiler)

#ç)önemli_bilgiler isimli sözlükte sağlık bakanlığı iletişim merkezi olup olmadığını kontrol edin:

kontrol=onemli_bilgiler.get("sağlık bakanlığı iletişim merkezi")
print(kontrol)
