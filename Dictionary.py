#Introduction
list_data = [1,2,3,4] #index 0,1,2,3
#Kumpulan data yang terdiri atas pasangan key dan value
#Key -> seperti index di list -> dipakai sebagai identifier data

#Berikan nama yang jelas
#Template dictionary
""" nama_dictionary = {
    'key':'value',
    'key2':'value',
    'key n':'value n',
}
print(nama_dictionary) """

#Untuk mengambil data d dictionary
#nama_dictionary['key']
#print(nama_dictionary['key'])
'''
data_murid1 = {
    'nama':'Amanda',
    'kelas':'XII RPL',
    'hobi':'Main game',
    'no_absen':'6',
    'nilai':90
}
data_murid2 = {
    'nama':'Arkan',
    'kelas':'XII IPA 2',
    'hobi':'Olahraga',
    'no_absen':'16',
    'nilai':90
}
data_murid3 = {
    'nama':'Orang',
    'kelas':'XII JB 1',
    'hobi':'Memasak',
    'no_absen':'2',
    'nilai':80
} '''
#print(data_murid2)
""" data_murid1 = {
    'nama':'Amanda',
    'kelas':'XII RPL',
    'hobi':'Main game',
    'no_absen':'6',
    'nilai':90,
    'isActive': True
}
print(data_murid1)
print("\n") """

'''#Operasi Dictionary
#1. Menghitung panjang dictionary
panjang = len(data_murid1)
print("Panjang datanya: ",panjang)

#2. Mengecek apakah suatu data ada atau tidak
# nama_key in nama_dictionary
key ="nama"
check = key in data_murid1 #ngecek ada data itu
print("Data ada atau tidak? ",check)
check2 = "umur" not in data_murid1
print("Apakah data tidak ada? ",check2)

#3. Akses Value -> Mengambil data dengan get
print(data_murid1['nama']) #ini cara biasa
#atau bisa menggunakan get untuk membedakan antra dictionary atau data collection lain

#Template: nama_dictionary.get('nama_key')
print("Ambil data: ", data_murid1.get('umur',"DATA TIDAK ADA!!!"))

#4. Menambah data
#Template
#nama_dictionary["nama_key_baru"] = "value data baru"
data_murid1["alamat"] = "Bali"
print("Data murid baru",data_murid1)

#5. Update data
#Tamplate:
""" nama_dictionary["nama_key_lama"] = "value baru" """
data_murid1['isactive'] = False
print("Update data murid",data_murid1)

#Update data yang lebih efisien (update data jika ditemukan atau menambah jika tidak ada)
#nama_dictionary.update(['key':'value'])
data_murid1.update({'tinggi':150})
print("Update data murid baru: ",data_murid1)

#CRUD (Create, Read, Update, Delete)
#Delete data
#Tamplate:
#del nama_dictionary['key']
del data_murid1['isactive']
print("Update data murid setelah delete: ",data_murid1) """

#Membuat dictionary tentang data stock (makanan)
""" print("="*68,"DATA MENU RUMAH MAKAN","="*68)
data_makanan1 = {
    'nama':'Bebek goreng',
    'bhn_utama':'Daging bebek',
    'lalapan':'Daun kemangi dan mentimun',
    'sambal':'Sambal bawang',
    'harga':25000
}
data_makanan2 = {
    'nama':'Lele goreng',
    'bhn_utama':'Ikan lele',
    'lalapan':'mentimun dan kol',
    'sambal':'Sambal bawang',
    'harga':20000
}
data_makanan3 = {
    'nama':'Ayam bakar',
    'bhn_utama':'Daging ayam',
    'lalapan':'Mentimun dan daun kemangi',
    'sambal':'Sambal kecap',
    'harga':25000
}
data_makanan4 = {
    'nama':'Belut goreng',
    'bhn_utama':'Daging belut',
    'lalapan':'Kol dan daun kemangi',
    'sambal':'Sambal bawang',
    'harga':17000
}
data_makanan5 = {
    'nama':'Sayur asem',
    'bhn_utama':'Labu siam, kulit tangkil, kacang panjang, melinjo, kol, jagung manis',
    'lalapan':'Mentimun',
    'sambal':'Sambal terasi',
    'harga':5000
}
print(data_makanan1,data_makanan2,data_makanan3,data_makanan4,data_makanan5) '''

#LOOPING
#1. Loop key-nya saja
#Cara pertama:
""" for variabel in nama_dictionary: 
    print(variabel) """

#2. Cara kedua:
""" for variabel in nama_dictionary.keys():
    do something """
#Jika ingin mengambil value-nya:
#nama_dictionary.get(variabel)

""" for murid in data_murid1.keys():
    print(murid,"|", data_murid1.get(murid))
 """
#2. Loop value-nya saja
""" for variabel in nama_dictionary.values():
    do something """
""" for murid in data_murid1.values():
    print(murid,"|",data_murid1.get(murid)) """

#3.Loop Items -> bisa milih mau keluarin key saja, value saja, atau keduanya
""" items = data_murid1.items()
print(items) """
""" for variabel in nama_dictionary.items():
    do something """
    
""" for key, value in data_murid1.items():
    print("Key: ",key,"| Value: ",value) """

#Nested Dictionary
#Cara pertama:
list_data = {
    'data_pertama' : {
        'nama':'Arkan',
        'umur':18,
        'alamat':'Serang',
    },
    'data_kedua' : {
        'nama':'Zayed',
        'umur':9,
        'alamat':'Jakarta'
    }
}
print(list_data)

#Cara kedua:
data_pertama = {
    'nama':'Arkan',
    'umur':18,
    'alamat':'Serang'
}
data_kedua = {
    'nama':'Zayed',
    'umur':9,
    'alamat':'Jakarta' 
}
kumpulan_data = {
    'data1':data_pertama,
    'data2':data_kedua
}
print(kumpulan_data)
