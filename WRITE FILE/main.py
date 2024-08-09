#1. Write
#Akan menimpa (overwrite)

with open("data1.txt","w",encoding="utf-8") as file:
    file.write("Saya ingin pergi ke Tiongkok lalu cari")

with open("data2.txt","w",encoding="utf-8") as file:
    file.write("Kemudian saya pergi ke Swiss\n")
    
with open("data1.txt","w",encoding="utf-8") as file:
    file.write("Saya ingin bermain bola bersama teman mahasiswa")

#2. Append (Menambah tulisan/tidak overwrite)
with open("data2.txt","a",encoding="utf-8") as file:
    file.write("Kemudian saya pergi ke Swiss\n")
    
with open("data2.txt","a",encoding="utf-8") as file:
    file.write("Saya menambah text dengan append di bahasa ular")

#3. Cara 3: r+ (overwrite sesuai dengan panjang baris nya)
with open("data-3.txt","w",encoding="utf-8") as file:
    file.write("Ini data ketiga")
    
with open("data-3.txt","r+",encoding="utf-8") as file:
    file.write("Ini baris pertama\n")
    file.write("Ini baris kedua\n")
    file.write("Ini baris ketiga\n")

with open("data-3.txt","r+",encoding="utf-8") as file:
    data = file.read()
    print(data)


with open("data-3.txt","r+",encoding="utf-8") as file:
    file.write("Haloo")