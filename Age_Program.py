import datetime as dt

tanggal = int(input("Tanggal lahir : "))
bulan = int(input("Bulan lahir : "))
tahun = int(input("Tahun lahir : "))

#menampilkan tanggal
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print("Tanggal lahir Anda adalah : ", tanggal_lahir)
print(f"Hari lahir Anda adalah : {tanggal_lahir:%A}")

#menghitung umur
today = dt.date.today()
print("Hari ini tanggal : ", today)
umur_hari = today-tanggal_lahir
umur_tahun = umur_hari.days//365 #floor division
umur_bulan = (umur_hari.days%365)//30
print("Umur hari Anda adalah : ", umur_hari)
#print("Umur Anda adalah ", umur_tahun, " Tahun", umur_bulan, " Bulan")
print(f"Umur Anda adalah {umur_tahun} Tahun {umur_bulan} Bulan")

