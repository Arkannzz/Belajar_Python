import datetime
import random
import string
import os
film_dict = {
    'judul':'JUDUL',
    'tanggal':datetime.datetime(1111,1,11),
    'bahasa':'BAHASA',
    'genre':'GENRE',
    'rating': 4.5
}

list_film = {}
while True:
    os.system("cls")
    print("="*30,"DATA FILM","="*30)
    film = dict.fromkeys(film_dict.keys())
    film['judul'] = input("Masukkan judul film: ")
    tanggal = int(input("Masukkan tanggal rilis: "))
    bulan = int(input("Masukkan bulan rilis: "))
    tahun = int(input("Masukkan tahun rilis: "))
    film['bahasa'] = input("Masukkan bahasa film: ")
    film['genre'] = input("Masukkan genre film: ")
    film['rating'] = float(input("Masukkan rating film: "))
    film['rilis'] = datetime.datetime(tahun,bulan,tanggal)
    key = ''.join(random.choice(string.ascii_uppercase) for i in range(3))
    list_film.update({key:film})


    #Menampilkan data
    print(f"{'key':<6}{'judul':<18}{'rilis (mm/dd/yy)':<18}{'bahasa':<11}{'genre':<10}{'rating '}")
    print("="*70)
    for movie in list_film:
        key = movie
        judul = list_film[key]['judul']
        rilis = list_film[key]['rilis'].strftime("%x")
        bahasa = list_film[key]['bahasa']
        genre = list_film[key]['genre']
        rating = list_film[key]['rating']
        print(f"{key:<6}{judul:<18}{rilis:<18}{bahasa:<11}{genre:<10}{rating }")
    pertanyaan = input("Apakah ingin menambahkan data? y/n: ")
    if pertanyaan == "n":
        break
print("Terima kasih sampai jumpa!!!")
