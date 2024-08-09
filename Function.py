#Function (Fungsi)
#Contoh: Membuat program penjumlahan
#Menyimpan kode yang berulang suoaya bisa dipakai lagi (reusable)
#Kalau mau pakai tinggal dipanggil
#Gampangnya kayak variabel tapi, nyimpen kode
#1. Memudahkan diri sendiri
#2. Memudahkan orang lain
#3. Memudahkan komputer

#Cara membuat:
# def nama_fuction():
#     isi function

# #Cara memanggil function
# nama_function()

#Function harus dibuat dulu sebelum dipanggil

# def greeting():
#     print("Hello")
#     print("Arkan bermain futsal di liga nusantara jawa barat")
    
# greeting()

#Jenis function
#1. Function dengan argument/parameter
#Nilai/data yang diperlukan komputer sebelum menjalankan function
#Cara nulis:
# def nama_function(argumen/data/parameter; berupa variabel):
#     isi function

# nama_function(isi data/isi parameter)
    
#Cara pake:
# def greeting(nama, umur):
#     print("Hello",nama, "Umurnya", umur)
    
#greeting("Arkan")
# greeting("Arkan", 24)

#Function dengan list
# def greeting(list_peserta):
#     data_peserta = list_peserta.copy()
#     for peserta in data_peserta:
#         print("Hello", peserta)
    
# murid = ["Amanda","Arkan","Budi","Rai","Ayu","Komang"]
# greeting(murid)

#Definisikan tipe data dalam function
# def nama_function(argumen/data/parameter:tipe_data):
#     isi function

# def greeting(nama, umur:int):
#     print("Hello",nama, "Umurnya", umur)
    
# greeting("Arkan", 24)

#2. Function dengan Return
# Dapat mengembalikan nilai
# def nama_function(argument):
#     do something
#     return output

# def kuadrat(angka):
#     hasil = angka**2 #pangkat 2
#     return hasil

# #Memanggil function kuadrat
# print(kuadrat(4))
# y = kuadrat(5)
# z = 10 + kuadrat(6)
# print(y)
# print(z)

#- Jika argumennya ada dua atau lebih
# def nama_function(argument1, argument2, argument-n):
#     do something
#     return output

# def penjumlahan(angka1, angka2):
#     return angka1 + angka2

# a = penjumlahan(7,8)
# print("Fungsi penjumlahan: ",a)

# def kalkulator(angka1,angka2):
#     tambah = angka1 + angka2
#     kurang = angka1 - angka2
#     kali = angka1*angka2
#     bagi = angka1 / angka2
#     return tambah,kurang,kali,bagi

# k,l,m,n = kalkulator(3,5)
# print("Hasil penjumlahan", k)
# print("Hasil pengurangan", l)
# print("Hasil perkalian", m)
# print("Hasil pembagian", n)

#Memberi tipe data yang spesifik untuk function
# def nama_function(argument:data_type) -> tipe_data:
#     isi function 
#     return output

# def pembagian(angka1, angka2:int) -> int:
#     return float(angka1/angka2)

# q = pembagian(6,2)
# print(q)

#3. Function dengan default argument
#- Jika argument kosong, dia akan pakai argument default
# def nama_function(argument = default_value):
#     isi function

def greeting(nama = "NAMA KAMU SIAPA !!??"):
    print("Halo, ", nama)
    
greeting()

def hitung_jumlah(angka1 = 0, angka2 = 0):
    return angka1 + angka2

result = hitung_jumlah(50000,6000)
print(result)


#Anaknya variabel
#1. Global Scope Variabel
    #Bisa diakses darimanapun

nama = "orang" #Global variabel
def fungsi1():
    print(nama)
    
fungsi1() 
    
#2. Local Scope Variabel
    #Variabel ini hanya dapat diakses dari dalam fungsi, tidak dapat diakses dari luar
    
def fungsi2():
    name = "Saya manusia" #cuma fungsi2 yang punya
    


#Ubah variabel global dari dalem fungsi
angka = 0
def ubah_angka(nilai_baru):
    global angka #gunction akan mendapat akses untuk mengganti data variabel global dari dalam fungsi
    angka = nilai_baru #mengganti data dari function
    
    
print("Angka sebelum: ", angka)
ubah_angka(15)
print("Angka sesudah: ", angka)




