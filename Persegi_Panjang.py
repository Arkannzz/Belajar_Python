def input_pp():
    while True:
        panjang = float(input("Silahkan masukkan panjangnya: "))
        lebar = float(input("Silahkan masukkan lebarnya: "))
        if panjang != 0 and lebar != 0:
            return panjang, lebar
            break
        else:
            print("Panjang atau lebar tidak boleh 0")

def keliling_pp(panjang, lebar):
    return 2*(panjang+lebar)

def luas_pp(panjang, lebar):
    return panjang*lebar

def result_pp(kalimat, hasil):
    print(kalimat, hasil)

def hitung_pp():
    option = input("Mau menghitung luas atau keliling?: ")
    panjang, lebar = input_pp()
    if option == "luas":
        luas = luas_pp(panjang, lebar)
        result_pp("Luasnya adalah: ", luas)
    if option == "keliling":
        keliling = keliling_pp(panjang, lebar)
        result_pp("Kelilingnya adalah: ", keliling)