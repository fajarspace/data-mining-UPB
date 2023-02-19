# a = input('Masukkan nilai A :')
# b = input('Masukkan nilai B :')
# print(a,b)

# print(1, 3, 5, 7)
# output: 1 3 5 7

#percabangan

# angka = 4
# if angka > 0:
#     print(angka, 'adalah bilangan positif')

# bilangan = -1
# if bilangan >= 0:
#     print('Positif atau nol')
# else:
#     print('Bilangan negatif')

# bilangan = 5.5
# if bilangan > 0:
#     print('Positif atau nol')
# elif bilangan == 0:
#     print('Nol')
# else:
#     print('Bilangan negatif')

# nomor = [5, 5, 2]
# jumlah = 0
# for tampung in nomor:
#     jumlah = jumlah + tampung
# print ('jumlah semuanya :', jumlah)

# for hitung in range(5):
#     print('Hitung :', hitung)

# hitung = 0
# while (hitung < 5):
#     print('hitung :', hitung)
#     hitung = hitung + 1

# i = 0
# n = int(input('Masukkan batas :'))
# for i in range(n):
#     if i%2 == 0:
#         print("Bilangan :", i)
#     i = i + 1

# def sapa(nama):
#     print('hai,' + nama +  '. Apa kabar?')
#     return nama
# sapa('Anna')

def persegipanjang(panjang, lebar):
    luas = panjang * lebar
    print('Luasnya :', luas)
    return luas

print('menghitung luas persegi panjang')
a = int(input('Masukkan panjang :'))
b = int(input('Masukkan lebar :'))
persegipanjang(a, b)