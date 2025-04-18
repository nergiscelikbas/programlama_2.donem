k1=int(input("1.kenarı girin:"))
k2=int(input("2.kenarı girin:"))
k3=int(input("3.kenarı girin:"))

if k1==k2 and k2==k3:
    print("eşkenar")
elif k1==k2 or k2==k3 or k3==k1:
    print("ikizkenar")
else:
    print("çeşitkenar")