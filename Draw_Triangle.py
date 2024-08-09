sisi = int(input("Masukkan sisinya : "))
count = 1
""" print("-----Segitiga For-----")
for i in range(sisi):
    print("*"*count)
    count=count+1 #untuk gambar ke kanan
    
print("-----Segitiga While-----")
count_while = 1
while True:
    print("*"*count_while)
    count_while=count_while+1
    if count_while>sisi:
        break
    
print("-----Segitiga Ganjil-----")
count_ganjil = 1
while True:
    if count_ganjil%2 == 1:
        print("*"*count_ganjil)   
        count_ganjil=count_ganjil+1
    else:
        count_ganjil=count_ganjil+1
        continue
    if count_ganjil>sisi:
        break """
    
print("-----Segitiga Sama Kaki-----")
count_sk = 1
jarak = int(sisi/2)
while True:
    if count_sk%2 == 1:
        print(" "*jarak,"$"*count_sk)
        jarak=jarak-1
        count_sk=count_sk+1
    else:
        count_sk=count_sk+1
        continue
    if count_sk>sisi:
        break
        
    
        