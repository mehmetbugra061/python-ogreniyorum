def Topla(x, y):
   return x + y
 
def Cikar(x, y):
   return x - y
 
def Carp(x, y):
   return x * y
 
def Bol(x, y):
   return x / y
 
print("Yapılacak İşlemi Seçin.")
print("=======================")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")
 
secim = input("Seçiminiz (1/2/3/4):")
 
sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
 
if secim == '1':
   print(sayi1,"+",sayi2,"=", Topla(sayi1,sayi2))
 
elif secim == '2':
   print(sayi1,"-",sayi2,"=", Cikar(sayi1,sayi2))
 
elif secim == '3':
   print(sayi1,"*",sayi2,"=", Carp(sayi1,sayi2))
 
elif secim == '4':
   print(sayi1,"/",sayi2,"=", Bol(sayi1,sayi2))
else:
   print("Geçersiz Giriş")