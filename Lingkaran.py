def input_ling():
    while True:
        jari = float(input("Silahkan masukkan jari-jarinya: "))
        if jari != 0:
            return jari
            break
        else:
            print("Jari-jari tidak boleh 0")
          
def keliling_ling(jari):
    return 2*3.14*jari

def luas_ling(jari):
    return 3.14*jari*jari

def result_ling(kalimat, hasil):
    print(kalimat, hasil)

def hitung_ling():
    option = input("Mau menghitung luas atau keliling?: ")
    jari = input_ling() 
    if option == "luas":
        luas = luas_ling(jari)
        result_ling("Luasnya adalah: ", luas)    
    if option == "keliling":
        keliling = keliling_ling(jari)
        result_ling("Kelilingnya adalah: ", keliling) 