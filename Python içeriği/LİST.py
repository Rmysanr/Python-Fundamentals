#LİSTELER:
"""
best_heavy_weigths=["Mike tyson","Muhammed Ali", "Lenox Lewis", "Evander Holyfield"]
for boxer in best_heavy_weigths:
    print(boxer)
"""
#Kullanıcıdan aldığımız bir ismin liste içerisinde var mı yok mu anlamak için bir algoritma yapalım
"""
isim= input("Bir isim giriniz: ")
best_heavy_weigths=["Mike Tyson","Muhammed Ali", "Lenox Lewis", "Evander Holyfield"]
sss
if isim== "Mike Tyson" :
    print("Mike Tyson listede vardır")
elif isim== "Muhammed Ali":
    print("Muhammed Ali listede vardır")
elif isim== "Lenox Lewis":
    print ( "Lenox Lewis listede vardır")
elif isim== "Evander Holyfield":
    print("Evander Holyfield listede vardır")
else:
    print(f" {isim} listede yoktur")
"""
# KISAA YOLU:
"""
isim= input("Bir isim giriniz: ")
best_heavy_weigths=["Mike Tyson","Muhammed Ali", "Lenox Lewis", "Evander Holyfield"]
for boxer in best_heavy_weigths:
    if boxer == isim :
        print (f"{isim} listede var")
        break
else:
    print(f"{isim} listede yok")
"""

#aynı sorunun kaçıncı index olduğunu da yazan bri algoritma yazalım

"""
isim= input("Bir isim giriniz: ")
best_heavy_weigths=["Mike Tyson","Muhammed Ali", "Lenox Lewis", "Evander Holyfield"]
for boxer in best_heavy_weigths:
    if boxer == isim :
        if isim== "Mike Tyson":
            print("0. index")
            break
        elif isim =="Muhammed Ali":
            print("1. index")
            break
        elif isim== "Lenox Lewis":
            print("2. index")
            break
        elif isim=="Evander Holyfield":
            print("3. index")
            break
else:
    print(f"{isim} listede yok")
    
"""

