import os

def judul():
    os.system("cls")
    print("="*20,"PROGRAM MENGHITUNG LUAS & KELILING PERSEGI PANJANG","="*20)

def input_user():
    PANJANG = float(input("Silahkan masukkan panjang: "))
    LEBAR = float(input("Silahkan masukkan lebar: "))
    return PANJANG, LEBAR
    
def keliling(panjang, lebar):
    return 2*(PANJANG+LEBAR)
    
def luas(panjang, lebar):
    return PANJANG*LEBAR

def result(kalimat, hasil):
    print(kalimat, hasil)
    
while True:
    judul()
    option = input("Mau menghitung luas atau keliling?: ")
    PANJANG, LEBAR = input_user()  
    if option == "luas":
        LUAS = luas(PANJANG, LEBAR)
        result("Luasnya adalah: ", LUAS)
    if option == "keliling":
        KELILING = keliling(PANJANG, LEBAR)
        result("Keliling adalah: ", KELILING)
    pertanyaan = input("Apakah ingin menghitung lagi? y/n: ")
    if pertanyaan == "n":
        break
print("PROGRAM SELESAI !!!")