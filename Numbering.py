angka = float(input("Masukkan angka yang kurang dari 3 atau lebih besar dari 10 : "))
kurang_dari = angka<3
print("Kurang dari 3 : ", kurang_dari)

lebih_dari = angka>10
print("Lebih dari 10 :", lebih_dari)

hasil = kurang_dari or lebih_dari
print("Angka yang dimasukkan adalah : ", hasil)

print("\n", 60*"=", "\n")

Angka = float(input("Masukkan angka yang lebih besar dari 3 dan lebih kecil dari 10 : "))
lebih_dari = Angka>3
print("Lebih dari 3 : ", lebih_dari)

kurang_dari = Angka<10
print("Kurang dari 10 : ", kurang_dari)

hasil = lebih_dari and kurang_dari
print("Angka yang dimasukkan adalah : ", hasil)

print("\n", 60*"=", "\n")

'''
-------0++++++5-------8++++++++11-------
'''

angka_satu = float(input("Masukkan angka yang lebih besar dari 0 dan lebih kecil dari 5 : "))
angka_dua = float(input("Masukkan angka yang lebih besar sama dengan 8 dan lebih kecil dari 11 : "))

Lebih_Dari = angka_satu>0
print("Lebih dari 0 : ", Lebih_Dari)

Kurang_Dari = angka_satu<5
print("Kurang dari 5 : ", Kurang_Dari)

hasil_satu = Lebih_Dari and Kurang_Dari
print("Angka yang dimasukkan adalah : ", hasil_satu)

print("\n", 60*"=", "\n")

lebih_dari_8 = angka_dua>=8
print("Lebih besar dari sama dengan 8 : ", lebih_dari_8)

kurang_dari_11 = angka_dua<11
print("Kurang dari 11 : ", kurang_dari_11)

hasil_dua = lebih_dari_8 and kurang_dari_11
print("Angka yang dimasukkan adalah : ", hasil_dua)
print("Kedua angka yang dimasukkan adalah : ", hasil_satu and hasil_dua)

