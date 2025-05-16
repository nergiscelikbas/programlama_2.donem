toplam=0
ogrenci_notlari=[]

for i in range(6):
    ogrenci_notlari.append(int(input("Not girin :")))

for ogr_not in ogrenci_notlari:
    toplam=toplam+ogr_not

ortalama=toplam/6

print("ortalamanız :",ortalama)