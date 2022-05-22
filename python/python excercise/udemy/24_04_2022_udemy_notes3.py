# -*- coding: utf-8 -*-
"""24.04.2022 udemy notes3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jCZADTsaGW1hOG2yWPa80h1lRdHqvM2_
"""

print("oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adı: ")
soyad = input("Oyuncunun Soyadı: ")
takım = input("Oyuncunun Takımı: ")

Bilgiler = [ad, soyad, takım]
print("Bilgiler kaydediliyor......")

print("Oyuncunun Adı: {}\nOyuncunun Soaydı: {}\nOyuncunun Takımı: {}\n".format(Bilgiler[0], Bilgiler[1], Bilgiler[2]))

print("Bilgiler Kaydediliyor.....")

""""
2.dereceden bir bilinmeyenli denklemin köklerini bulma
Denklem : ax^2 + bx + c
Deltayı Hesaplama : b ** 2 - 4 * a * c
Birinci Kök : (-b - delta ** 0.5) / (2 * a)
İkinci Kök : (-b + delta ** 0.5) / (2 * a)
"""
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
delta = b ** 2 - 4 * a * c
x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)
print("Birici Kök :{}\nİkinici Kök: {}\n".format(x1, x2))

# Problem 1
# Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.
a = int(input("Birinci Sayıyı Giriniz:"))
b = int(input("İkinci Sayıyı Giriniz:"))
c = int(input("Üçüncü Sayıyı Giriniz:"))
print("çarpım sonucunuz {}\n ". format(a *b * c))

# 2.yol
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

çarpım = a * b * c

print("{} x {} x {} = {} dir".format(a,b,c,çarpım))

# Problem 2
# Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
# Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
boy = float(input("Boyunuz:"))
kilo = float(input("Kilonuz:"))
print("Beden Kitle Endeksiniz:{}\n".format(kilo/(boy*boy)))

boy = float(input("Boy:"))
kilo = int(input("Kilo:"))

print("Beden Kitle İndeksi:",kilo / (boy ** 2))

# Problem 3
# Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın
birim_yol = float(input("yapmış olduğunuz km:"))
birim_yakıt = float(input("yakıt miktarı lt:"))
print("km başına yakılan yakıt: {}".format(birim_yakıt/birim_yol))

yakan_miktar = float(input("Kilometrede yakan miktar:"))

kilometre = int(input("Kaç km yol yaptınız:"))

print("Tutar: {} tl".format(yakan_miktar * kilometre))

# Problem 4
# Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
Adı = (input("Adınız: "))
Soyadı = (input("Soyadınız: "))
iletişim = int(input("iletişim Bilgilerinizi"))
print("Adınız:{}\nSoyadınız:{}\niletişim Bilgileriniz:{}".format(Adı, Soyadı, iletişim))

ad = input("Ad:")
soyad = input("Soyad:")
numara = input("Numara:")
print("\nBilgiler...\n")
print("{}\n{}\n{}".format(ad,soyad,numara))

# Problem 5
# Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
a = int(input("Birinci Sayıyı Giriniz:"))
b = int(input("İkinici Sayıyı Giriniz: "))
print("Birinci Sayının değeri:{}\nİkinci Sayının değeri:{}".format(b, a))

a = input("a:")
b = input("b:")

print("Değiştirilmeden Önce Değerler\na: {} b: {}\n".format(a,b))

a,b = b,a

print("Değiştirildikten Sonraki Değerler\na: {} b: {}\n".format(a,b))

# Problem 6
# Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
# Hipotenüs Formülü: a^2 + b^2 = c^2
a = int(input("birinci kenar uzunluğunu giriniz:"))
b = int(input("İkinci kenar uzunluğunu giriniz:"))
c = ((a^2) + (b^2))^2
print("Hipetenüs Değeri:{}".format(c))

a = int(input("a:"))

b = int(input("b:"))

c =  (a ** 2 + b ** 2) ** 0.5

print("Hipotenüs: ",c)

print("79 karakteri gemiyoruz. geçersen de hata vermez ama kodun yana doğru uzar gir. \
burada olduğu gibi ters slash kullanarak alt satıra geçebiliyorsunuz. \
sanki tek satırda kalmış gibi ekrana yazdırdı.")
