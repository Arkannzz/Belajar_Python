'''
0 1
2 3
3 5
4 7
5 9'''

angka1 = 0
angka2 = 0
jarak = 1
while True:
    if angka1 < 6 and angka2 < 10 and angka2%2 == 1:
        print(angka1," "*jarak,angka2)
        angka1 = angka1 + 1
        angka2 = angka2 + 1
    else:
        angka2 = angka2 + 1
        continue
    if angka1 > 5 and angka2 > 9:
        break
    
number = 0
for i in range(0, 6):
    print(i, " ", i*2+1)
    

    
        
        