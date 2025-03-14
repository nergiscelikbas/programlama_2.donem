miktar=int(input("lütfen kg girin:"))
if miktar<=10:
    ucret=miktar*10
    print("ödeme:",ucret)

else:
    ucret=100+(miktar-10)*7.5
    print("ödeme:",ucret)