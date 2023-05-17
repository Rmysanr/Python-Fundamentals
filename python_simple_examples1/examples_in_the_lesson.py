#TUPLE:

my_family=[
    ('burak yılmaz',34,'beast'),
    ('hakan yılmaz',37,'bear'),
    ('ipek yılmaz',39,'keko')]

for x,y,z in my_family:
    print(f'full name: {x}\nage: {y}\nuser name: {z}')

#DİCTİONARY

release_year_movies={
    'fight club':1999,
    'matrix':1999,
    'interstaller':2014,
    'inception':2010,
    'dune':2021,
}
#herhangi bir filmin anahtarlarını çağararak değerlerini ekrana yazın

print(f'interstaller release year: {release_year_movies.get("interstaller")}')

#sözlüğün bütün anahtarlarını dökün.
print(f'movie list: {type(release_year_movies.keys())}')
for i in release_year_movies.keys():
    print(i)


#sözlüğün tüm değerlerini dökün:

for i in release_year_movies.values():
    print(i,end=' ')
print([i for i in release_year_movies])

#OR
from pprint import pprint
pprint({name:year for name, year in release_year_movies.items()})

products=[
    {'name':'everlast pro boxing gloves','price':245},
{'name':'everlast training gloves','price':200},
{'name':'everlast havy bag','price':345},
{'name': 'everlast hand_wrap','price':56},
{'name':'ıphone 14 pro max','price':4800},
{'name':'samsung g20','price':40000},
{'name':'lenovo xl carbon','price':49000},]

#products listesindeki bütün fiyatları toplayarak ekrana bastırın:

total_price=0
for products in products:
    total_price+=products.get('price')
print(f'total:{total_price}')


#products listesindeki ürün fiyatı 30000'den büyük olan ürünlerin isimlerini listeleyin.
ürün_listesi=[]
for products in products:
    ürün_listesi=products.get('price')
    if ürün_listesi>=30000:
        print(ürün_listesi)
#ya da :

for products in products:
    if products['price']>=30000:
        print(products['name'])


#ürün adı içerisinde everlast geçen ve fiyat aralığı 150 ile 300 arasında olan ürünleri listeleyelim.


ürün_listesi=[]
fiyat=[]
for products in products:
    if 'everlast' in products['name'] and (150 <= products['price']<=300):
        print(products['name'])