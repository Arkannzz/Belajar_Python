#Try & Except (Try and Catch)
#Untuk membuat program terus berlanjut meskipun ada runtime error
#Except akan menangkap error-nya 
#Pola:
# try:
#     apa yang mau di-tes
# except:
#     apa yang terjadi saat error
    
#Contoh 1
data = int(input("Masukkan angka: "))
hasil = 0
try:
    hasil = 10*data
except:
    print("Angka tidak boleh 0")
print(hasil)

#Contoh 2: Bentuk aplikasi
# while True:
#     data = int(input("Masukkan angka: "))
#     hasil = 0
#     try:
#         hasil = 10/data
#         print(hasil)
#         done = input("Mau lanjut? (y/n): ")
#         if done == "n":
#            break
    
#     except:
#         print("Angka tidak boleh 0")
# print("AKHIR PROGRAM 2")

# #Contoh 3: Membuka file
# try:
#     with open("hello world.txt","r") as file:
#         print(file.read()) #kalo file nya ada, akan membaca/meng-print isinya si file txt
# except:
#     print("File tidak ditemukan. Akan membuat file baru")
    
#     #membuat file kosong
#     with open("hello world.txt","w",encoding="utf-8") as file: #encoding: bentuk karakter
#         file.write("Halo dunia, saya lagi belajar. Setelah belajar saya akan main game.")
   
    
        