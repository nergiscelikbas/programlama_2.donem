hava_durumu=int(input("hava sıcaklığını girin:"))
if hava_durumu<=5:
    print("soğuk")
elif hava_durumu>=6 and hava_durumu <=14:
    print("ılık")
else:
    print("sıcak")