#Looping
#1. Looping yang bisa dihitung (Looping yang pasti jumalahnya)

#Ditulis dengan range
'''for i in range(start, stop):
    aksi'''

for i in range(0, 20):
    print(i,". Hello arkan")
    
#2. Ditulis dengan list
'''for i in nama_list: #i untuk menyimpan
    aksinya'''
    
print("----For in List----")
listdata = [1,2,3,4,5]
for i in listdata:
    print(i)
    
#3. Menggunakan string
'''for i in data_string:
    aksi'''
    
print("------String dalam for------")
data_str = "Hewan"
for i in data_str:
    print(i)
    
    