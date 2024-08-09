data_game1 = {
    'nama':'Call of Duty: Black Ops III',
    'tahun_rilis':2015,
    'genre':'Action',
    'OS':'Windows 7',
    'penyimpanan':'100 GB'
}
data_game2 = {
    'nama':'Apex Legends',
    'tahun_rilis':2020,
    'genre':'Shooter',
    'OS':'Windows 10',
    'penyimpanan':'75 GB'
}
data_game3 = {
    'nama':'Tekken 8',
    'tahun_rilis':2024,
    'genre':'Arcade',
    'OS':'Windows 10',
    'penyimpanan':'100 GB'
}
kumpulan_game = {
    'data1':data_game1,
    'data2':data_game2,
    'data3':data_game3
}
print(f"{'key':<6}{'Nama':<28}{'Tahun':<6}{'Genre':<8}{'OS':<12}{'Storage '}")
print(67*"=")
for game in kumpulan_game:
    key = game
    nama = kumpulan_game[key]['nama']
    tahun = kumpulan_game[key]['tahun_rilis']
    genre = kumpulan_game[key]['genre']
    os = kumpulan_game[key]['OS']
    storage = kumpulan_game[key]['penyimpanan']
    print(f"{key:<6}{nama:<28}{tahun:<6}{genre:<8}{os:<12}{storage}")