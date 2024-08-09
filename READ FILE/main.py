#Read file eksternal

#Cara 1: Open

file = open("data.txt",mode="r")

print("Status Readable: ",file.readable())
print("Status Writable: ",file.writable(),"\n")

#Membaca seluruh file
#print(3*"=","Membaca seluruh file",3*"=")
#print(file.read())

#Membaca per baris
# print(3*"=","Membaca per baris",3*"=")
# print(file.readline(),end="")
# print(file.readline())

#Membaca seluruh baris sebagai list
print(3*"=","Membaca seluruh baris sebagai list",3*"=")
print(file.readlines())

#Menutup File
print("Apakah file sudah di close?", file.closed, "\n") #akan mengecek file sudah ditutup atau belum
file.close() #akan menutup file

#Cara kedua: With, membuka dan menutup file otomatis
print(3*"=","Membaca dengan with",3*"=")
with open("data.txt",mode="r") as file:
    data = file.read()
    print(data)
