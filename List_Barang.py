list_barang = []
while True:
    nama = input("Masukkan nama barang: ")
    stok = int(input("Masukkan jumlah stok barang: "))
    kategori = input("Masukkan kategori barang: ")
    harga = int(input("Masukkan harga barang: "))

    barang_baru = [nama,stok,kategori,harga]
    list_barang.append(barang_baru)
    print("="*20,"DATA SUPERMARKET","="*20)
    for index,barang in enumerate(list_barang):
        print(index + 1,"Nama:",barang[0],"|Stok:",barang[1],"|Kategori:",barang[2],"|Harga:",barang[3])
    pertanyaan = input("Apakah mau dilanjutkan y/n: ")
    if pertanyaan == "n":
        break
print("Program Selesai Terima kasih :)")

      
    
    

