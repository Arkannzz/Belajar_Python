#membuat program menyimpan data game
"""
1. nama
2. genre
3. support offline/online
4. sistem operasi (windows,macios,linux)"""

list_game = []
while True:
    nama = input("Masukkan nama game: ")
    genre = input("Masukkan genre game: ")
    support = input("Apakah game online? y/n: ")
    operasi = input("Masukkan sistem operasi game: ")
    if support == "y":
        support = True
    elif support == "n":
        support = False
    game_baru = [nama,genre,support,operasi]
    list_game.append(game_baru)
    print("="*20,"DATA GAME","="*20)
    for index,game in enumerate(list_game):
        print(index + 1,"Nama:",game[0],"| Genre:",game[1],"| Support:",game[2],"| Sistem Operasi:",game[3])
    pertanyaan = input("Apakah mau dilanjutkan y/n: ")
    if pertanyaan == "n":
        break
print("Program Selesai Terima kasih :)")


