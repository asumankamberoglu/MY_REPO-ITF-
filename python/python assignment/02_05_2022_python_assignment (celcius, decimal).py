# -*- coding: utf-8 -*-
"""02.05.2022 python assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12l8lM_iS31Tr3LWVwCQ4d_v6i9n826ey
"""

# Write a short Python program that asks the user to enter Celsius temperature
# (it can be a decimal number), converts the entered temperature into
# Fahrenheit degree and prints the result.

Celsius = float(input('Sıcaklık değerini Celcius cinsinden girin: '))

# Celsius = (Fahrenheit – 32) * 5/9 # Fahrenheit girilip Celcius istenseydi...
Fahrenheit = (Celsius * 9/5) + 32

print("Sıcaklık", Fahrenheit, "°F")

Celsius = float(input('Sıcaklık değerini Celcius cinsinden girin: '))

Fahrenheit = (Celsius * 9/5) + 32

print("Sıcaklık", Fahrenheit, "°F")

# Write a short Python program that asks the user to enter a distance (it can
# be a decimal number) in kilometers, converts the entered distance into miles
# and prints the result.

# Kullanıcıdan mesafeyi km cinsinden iste
kilometre = float(input("Mesafeyi km cinsinden girin: "))

# conversion factor (dönüştürme katsayısı)
donusturme_katsayisi = 0.621371

# Mesafeyi mil cinsinden hesapla
mil = kilometre * donusturme_katsayisi
print('%0.2f kilometre %0.2f mil mesafeye eşittir.' % (kilometre, mil))

kilometre = float(input("Mesafeyi km cinsinden girin: "))

donusturme_katsayisi = 0.621371

mil = kilometre * donusturme_katsayisi
print('%0.2f kilometre %0.2f mil mesafeye eşittir.' % (kilometre, mil))

#değer değiştirme metodu
x=1
y=5
if x < y:
    z = y - x
    print(x + z)
    print(y + (-1 * z))
else:
    z = (x - y)
    print(x + (-1 * z))
    print(y + z)

x=5
y=1
if x < y :
    z = y - x
    print('x = ' + str(x + z))
    print('y = ' + str(y + (-1 * z)))
else:
    z = (x - y)
    print('x = ' + str(x + (-1 * z)))
    print('y = ' + str(y + z))

yağış_türleri = ("kar dolu yağmur")
print(yağış_türleri)
type(yağış_türleri)

yağış_türleri = "kar", "dolu", "yağmur"
print(yağış_türleri)
type(yağış_türleri)

yağış_türleri = ['kar', 'dolu', 'yağmur']
print(yağış_türleri)
type(yağış_türleri)

for i in range(1, 10, 2):
  islem = i * 2 + 5
  print(i)
  print(islem)
print("end of the for loop")

