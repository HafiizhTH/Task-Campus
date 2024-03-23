while True:
    print("+====================================================+")
    print("| NIM : 2012500720                               |")
    print("| Nama : Hafiizh Taufiqul Hakim                  |")
    print("| Program untuk mencetak nilai tengah            |")
    print("| dari tiga buah nilai yang di input             |")
    print("+====================================================+\n")
    i = 0
    while i < 1:
        print("\nInput 3 Angka : ")
        a = int(input("Angka 1 : "))
        b = int(input("Angka 2 : "))
        c = int(input("Angka 3 : "))
        if (a==b or a==c or b==c):
            print("\nAngka tidak boleh sama")
        else:
            i+=1

    bilangan = [a, b, c]
    if len(bilangan)%2 == 0:
        tengah1 = len(bilangan)//2-1
        tengah2 = tengah1+1
        print("Nilai Tengah : ", (bilangan[tengah1]+bilangan[tengah2])/2)
    else:
        tengah = len(bilangan) // 2
        print("\nNilai Tengah : ", bilangan[tengah])

    if input('\nLanjut ? (y/t) : ') !='y':
        break