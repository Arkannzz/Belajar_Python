angka1 = float(input("Masukkan angka pertama : "))
angka2 = float(input("Masukkan angka kedua : "))
operator = str(input("Masukkan operator (+, -, x, :) : "))

if operator == "+":
    hasil = angka1 + angka2
    print("Hasilnya adalah : ", hasil)
    
elif operator == "-":
    hasil = angka1 - angka2
    print("Hasilnya adalah : ", hasil)
    
elif operator == "x":
    hasil = angka1 * angka2
    print("Hasilnya adalah : ", hasil)
    
elif operator == ":":
    hasil = angka1 / angka2
    print("Hasilnya adalah : ", hasil)
    
else:
    print("OPERATOR SALAH !!! MASUKKAN YANG BENAR !!!")
    
    
    