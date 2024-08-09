import os
import Persegi
import Persegi_Panjang
import Lingkaran

def judul():
    os.system("cls")
    print("="*10,"PROGRAM MENGHITUNG LUAS & KELILING BANGUN DATAR","="*10)

while True:
    judul()
    print("1. Persegi")
    print("2. Persegi panjang")
    print("3. Lingkaran")
    pilihan = int(input("Silahkan masukkan angka pilihan bangun datar: "))    
    if pilihan == 1:
        Persegi.hitung_persegi()
    elif pilihan == 2:
        Persegi_Panjang.hitung_pp()
    elif pilihan == 3:
        Lingkaran.hitung_ling()
    pertanyaan = input("Apakah ingin menghitung lagi? y/n: ")
    if pertanyaan == "n":
        break
print("PROGRAM SELESAI !!!")
    

        
    