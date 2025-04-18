ucret=int(input("otoparkın ücret tarifesini giriniz:"))
if ucret==1:
    print("5TL")
elif ucret<=5:
    print("ödenecek tutar:",ucret*4)
elif ucret>5:
    print("ödenecek tutar:",ucret*3)
else:
    print("hatalı")