#print("Halo nama saya arkan") #ini nama arkan
'''ini
comment multi line
'''
'''print("Belajar coding")
print("5 ?")
print('don\'t eat')'''

#manipulasi string
'''kalimat_1 = "saya arkan "
kalimat_2 = "makan pagi"
kalimat_3 = kalimat_1 + kalimat_2
print(kalimat_3)
print("kalimat 3 adalah", kalimat_3) #menggabungkan kalimat dengan variabel
print("panjang kalimat 3 adalah ", len(kalimat_3)) #ini menghitung karakter
print("wk"* 100)'''

#Tugas list game action
'''print("List game action:")
print("1. Free Fire")
print("2. Subway Surfers")
print("3. PUBG Mobile")
print("4. Call of Duty Mobile")
print("5. Brawl Stars")
print("6. Stumble Guys")
print("7. Shadow Fight")
print("8. Temple Run")
print("9. Mortal Kombat")
print("10. Fruit Ninja")'''

kalimat_1 = "saya arkan "
kalimat_2 = "makan pagi"
kalimat_3 = kalimat_1 + kalimat_2
print(kalimat_3)
print("arkan" not in kalimat_3) #untuk mencari yang tidak ada
print("makan" in kalimat_3) #untuk mencari yang ada
print("index ke 4 dari kalimat 3 adalah ", kalimat_3[5]) #mengambil data dengan index
print("index ke 5-9 dari kalimat 3 adalah ", kalimat_3[5:10]) #mengmabil data dengan index range
print("index ke 4 dari kalimat 3 adalah ", kalimat_3[-5]) #negatif indexing
print("index ke 4 dari kalimat 3 adalah ", kalimat_3[5:10:2]) #range indexing dengan interval
print("Jumlah huruf a pada kalimat 3 ada", kalimat_3.count("a")) #menghitung karakter tertentu
print("Uppercase", kalimat_3.upper()) #untuk membuat karakter kapital
print(".".join(kalimat_1))
print(kalimat_1.split("."))

text = "harganya {:,} rupiah"
print(text.format(2000000))

#tanggal
import datetime
tanggal = "29,3,2024"
print(datetime.date.today())
print(datetime.datetime.now())