while True:
    print("+====================================================+")
    print("| NIM : 2012500720                               |")
    print("| Nama : Hafiizh Taufiqul Hakim                  |")
    print("| Program untuk mencetak jenis segitiga          |")
    print("| dari tiga panjang sisi yang di input           |")
    print("+====================================================+\n")

    print("\nInput panjang 3 sisi : ")
    sisi1 = int(input("Sisi 1 : "))
    sisi2 = int(input("Sisi 2 : "))
    sisi3 = int(input("Sisi 3 : "))

    if(sisi1==sisi2 and sisi1==sisi3):
        print("\nSegitiga sama sisi")
    elif(sisi1==sisi2 or sisi1==sisi3):
        print("\nSegitiga sama kaki")
    else:
        print("\nSegitiga sembarang")

    if input('Lanjut ? (y/t) : ') !='y':
        break