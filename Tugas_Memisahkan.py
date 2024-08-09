#Tugas membuat list memisahkan angka ganjil dan genap

data_range = range(1,11)
list_data =list(data_range)
print("List data: ",list_data)

data_ganjil = [i for i in range(1,11) if i%2 == 1]
print("List data angka ganji: ",data_ganjil)

data_genap = [i for i in range(1,11) if i%2 == 0]
print("List data angka genap: ",data_genap)
