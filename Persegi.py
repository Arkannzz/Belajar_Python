
def input_p():
    while True:
        sisi = float(input("Silahkan masukkan sisinya: "))
        if sisi != 0:
            return sisi
            break
        else:
            print("Sisi tidak boleh 0 ")

def keliling_p(sisi):
    return 4*sisi  
    

def luas_p(sisi):  
    return sisi*sisi
   
def result_p(kalimat, hasil):
    print(kalimat, hasil)

def hitung_persegi():
    sisi = input_p()
    option = input("Mau menghitung luas atau keliling?: ")
    if option == "luas":
        luas = luas_p(sisi)
        result_p("Luasnya adalah: ", luas)
    if option == "keliling":
        keliling = keliling_p(sisi)
        result_p("Kelilingnya adalah: ", keliling)
        
# if sisi != 0
# raise ValueError

    
   
    
