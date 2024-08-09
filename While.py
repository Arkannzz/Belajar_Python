#Untuk perulangan yang entah gatau berapa kali (tidak pasti)

'''while kondisi: #kondisi true
    aksi 1
    aksi 2
    aksi n
akhir program #kondisi false'''

""" angka = 0
while angka < 5:
    print(angka)
    angka = angka + 1
print("Sudah cukup") """

#1. pass -->lewat/ga dianggap
'''angka = 0
while angka < 5:
    angka = angka + 1
    
    if angka == 3:
        pass #ngga dilakuin
    
    print(angka)
print("Sudah cukup")'''

#2. Continue -->lanjut/skip
""" angka = 0
while angka < 5:
    angka = angka + 1
    
    if angka == 3:
        continue #skip tapi lompat ke atas
    print("aku mau makan es krim vanilla")
    print(angka)
print("Sudah cukup") """

#3. Break -->istirahat/selesai
angka = 1
while angka < 5:
    
    if angka == 3:
        break #langsung selesai
    print("aku mau makan es krim vanilla")
    print(angka)
    angka = angka + 1
print("Sudah cukup")