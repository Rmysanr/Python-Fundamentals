

# x = "mike tyson"

#first_name = "Burak Yılmaz"

#print(first_name)

# Burada print() bulit-in fonksiyonu aracılığı ile değişken üzerinde tutulan ifadeyi ekrana yazdırdık.

#first_name = 10

# yukarıdaki satırda firs_name değişkenleri içerisine 10 değerini atadık Gördüğünüz gibi istediğimiz değeri değişken içerisinde atayabiliyoruz.Bu özlellik  c, c++, c#, java, PHP gibi programlama dillerinde bulunmaktadır.


#print(first_name) #print() algoritmada kullandığımız output olarak düşünebilirsiniz

#kullanıcıdan alınan iki adet sayı üzerinden temel 4 işlem yapan uygulama
#Kullanıcdan input alırken python içerisinde built-in olarak bulunan input() fonksiyonunu kullanıyoruz Daha sonra kullanıcıyı doğru yönlendirmek için içerisinde bir mesaj yazıyoruz.Lakin şunu unutmayalım kullanıcıdan her değer aldığımızda bize gelen valunun tipi string.
#Aritmetiksel işlem yapmak istediğimizde bize gelen değeri int değişken tipine dönüştürmemiz gerekmektedir.

#region example -1
#sayi_1 = int(input("Lütfen bir sayı giriniz: "))
#sayi_2 = int(input("Lütfen bir sayı giriniz: "))

#toplam = sayi_1 + sayi_2
#endregion

#region example -2
"""
#Kullanıcıdan alınan kenar bilgisine göre bir karenin alanını ve çevresini hesaplayan uygulmayı yazınız

kenar = int(input("Bir sayı giriniz: "))
#yukarıda kullanıcıdan alınan input int() fonsiyonu aracılığıyla int tipine dönüştürdük çünkü kullanıcıdan gelen değeri aritmatiksel ,işleme sokacağım
cevre = 4 * kenar
alan = kenar * kenar
print(f' karenin çevresi: {cevre}')
print(f' karenin alanı: {alan}')
"""
#endregion

#region example -3

#Kullanıcıdan alınan kısa ve uzun kenar bilgilerine göre bir dikdörtgenin alanını ve çevresini hesaplayalım

#kisa_kenar= int(input( "Bir sayı giriniz: "))
#uzun_kenar= int(input( "Bir sayı giriniz: "))

#cevre= kisa_kenar*2 + uzun_kenar*2
#alan= kisa_kenar * uzun_kenar
#print(f' dikdörtgenin çevresi : {cevre}')
#print(f' dikdörtgenin alanı : {alan}')

#2.yol;
#print(f' Alan: {x*y}') x kısa kenar y uzun kenar
#print(f' cevre: {2* (x+y)}')


#enderegion

#region example -4
#Üçgenin alanını hesaplayan uygulama yapalım
"""
taban= int(input("Bir sayı giriniz: "))
yukseklik = int(input( "Bir sayı giriniz: "))
alan = taban*yukseklik / 2
print(f' üçgenin alanı: {alan}')
"""











