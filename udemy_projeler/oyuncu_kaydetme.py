""""
print("oyuncu kaydetme programı.")
ad = input("oyunucunun adı: ")
soyadı = input("oyuncunun soyadı :")
takım = input("oyuncunun takımı: ")

bilgiler=[ad,soyadı,takım]

print("bilgiler kaydediliyor...")

print("oyuncunun adı: {}\nOyuncunun soyadı: {}\nOyuncunun takımı: {}\n".format(bilgiler [0],bilgiler[1],bilgiler[2]))

print ("bilgiler kaydediliyor...")

"""

a = int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

delta = b**2-4*a*c

x1 =(-b-delta**0.5)/(2*a)
x2 =(-b+delta**0.5)/(2*a)

print("birinci kök: {}\nikinci kök: {}\n".format(x1,x2))