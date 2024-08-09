""" angka = 0

#untuk menyimpan banyak data
listdata = [] #list kosong
listangka = [1,2,3,4,5,6,7,8,9,10,11.5]
print(listangka)

list_str = ["Amanda","Arkan","Zayed"]
print(list_str)

#data boolean
list_bool = [True, False, True, False]
print(list_bool)

#data campuran
list_gado_gado = [1,2,3,4,"makna","minum","belanja",True,False,False]
print(list_gado_gado)

#index list
#dimulai dari 0
list_str = ["Amanda","Arkan","Zayed"]

#Amanda -> 0
#Arkan -> 1
#dts

#data_range
data_range = range(0,101)
print("Data Range: ", data_range)
data_list = list(data_range) #ubah dari range ke list
print("Data List: ", data_list)

#list dengan For Loop
list_for = [i for i in range(0,10)]
print("Data list lopp for: ", list_for) """

""" #list For if
list_genap = [i for i in range(0,100)if i%2 == 0]
print("Data list for if: ",list_genap) """

#manipulasi data
#1. Mengambil data

list_genap = [i for i in range(0,100)if i%2 == 0]
print("Data list for if: ",list_genap)
print("Data ke-4: ",list_genap[4])

# #negative indexing
print("Data ke-(-2): ",list_genap[-2])

#2. Menambah data
print(10*"-")
# - nama_list.insert(posisi, datanya apa)
list_genap.insert(40, "x")
print("Data baru: ",list_genap)
# - nama_list.append(datanya apa)
print(10*"-")
list_genap.append("Finish")
print("Data terakhir: ",list_genap)
# - nama_list.extend(list_data_baru)
print(10*"-")
data_baru = "Saya membeli 50 es krim", "Tapi tokonya tutup", "Ami belajar coding bersama arkan"
list_genap.extend(data_baru)
print("Data extend: ", list_genap)

#3. Mengubah data
print(10*"-")
# nama_list(index ke berapa)
list_genap[3]="z"
print("Data Update 1.1: ",list_genap)

#4. Menghapus data
print(10*"-")
# nama_list.remove(data yang mau di hapus)
list_genap.remove("Tapi tokonya tutup")
print("Data remove: ",list_genap)

print(10*"-")
#nama_list.pop()
list_genap.pop()
print("Data pop: ",list_genap)


#OPERASI LIST
#1. Menghitung data muncul berapa kali
#nama_list.count(data yang mau dihitung)
""" angka = [1,2,3,4,5,5,5,5,6,7,7,7,7,7,8,10]
print(angka)
print("Angka ke 7 ada sebanyak: ", angka.count(7)) #menghitung jumlah angka 7 muncul berapa kali

#2. Mengambil posisi data (index)
print(10*"-")
#nama_list.index(datanya apa)
print("Angka 5 ada di index ke: ", angka.index(5)) #mendapatkan posisi data angka 5
#3. Mengurutkan list (ascending - bisa juga untuk karakter - A to Z)
print(10*"-")
angka2 = [10,5,6,7,7,7,7,7,0]
#nama_list.sort()
angka2.sort() #tidak boleh disatukan dengan print
print("Data yang diurutkan: ",angka2)
nama = ["Amanda", "Ayu", "Ayu Puspita", "Rai", "Cokorda", "Arkan"]
nama.sort()
print(nama)

#4. Membalikan urutan (descending/reverse - Z to A)
print(10*"-")
#nama_list.reverse()
nama.reverse()
print("Data descending: ", nama) """

#NESTED LIST

#perbedaan dengan Exntend
""" list_data = [1,2]
data2 = [3,4]
list_data.extend(data2) #daripada masukkin satu-satu
print("Entend List", list_data)

list_data = [1,2]
data2 = [3,4]
data_nama = ("Arkan", "Budi", "Ayu")
nested_list = [list_data, data2, data_nama, "Saya beli sayur" ]
print("Nested List: ",nested_list)
print("Data index ke-2: ",nested_list[2])
print("Data index ke-2-1: ",nested_list[2][1])

#cara penggunaan
data_mahasiswa = []
mahasiswa1 = ["Amanda",24,"Perempuan"]
mahasiswa2 = ["Amanda",24,"Laki-laki"]
mahasiswa3 = ["Bayu",2,"Laki-laki"]

data_mahasiswa = [mahasiswa1,mahasiswa2,mahasiswa3]

for index, mhs in enumerate (data_mahasiswa):
    print("Nama:\t",mhs[0])
    print("Umur:\t",mhs[1])
    print("Gender:\t",mhs[2],"\n") """

#LOOPING DENGAN LIST
#1. Dengan For
""" for nama_variabel in nama_list:
    aksi """

# print("="*20,"FOR LOOP","="*20)
# numbers = [1,2,3,4]
# for angka in numbers:
#     print("Angka: ", angka)
    
# #2. Loop dengan range
# print("="*20,"FOR LOOP DENGAN RANGE","="*20)
# kumpulan_angka = [3,4,6,5,8,9,10,2,4]
# panjang = len(kumpulan_angka)#menghitung panjang list
# for i in range(panjang): 
#     print("Angka: ", kumpulan_angka[i])
    
# #3. While
# '''while i < panjang:
#     aksi'''
    
# print("="*20,"WHILE LOOP","="*20)
# kumpulan_angka = [3,4,6,5,8,9,10,2,4]
# panjang = len(kumpulan_angka)
# i=0
# while i < panjang:
#     print("Angka: ", kumpulan_angka[i])
#     i = i + 1
    
# #4. List Comprehension
# #for in nama_list

# print("="*20,"LIST COMPREHENSION","="*20)
# data_list = [1,2,"buku","makanan",7,9]
# [print("Data ke-",i) for i in data_list] #ini polanya

# #5. Enumerate
# #mengambil index dan value (data)-nya langsung
# """ for index,nama_variabelnya in enumerate(nama_list-nya):
#     aksi
#  """

# data_list = [1,2,"buku","makanan",7,9]
# for index, dataku in enumerate(data_list):
#     print("Index ke-", index,":",dataku) #Index ke-n: datanya apa