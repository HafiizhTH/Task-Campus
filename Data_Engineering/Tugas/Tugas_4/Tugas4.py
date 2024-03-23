def main():
    field_list = ["NIM", "Nama", "Tugas", "UTS", "UAS"]
    list_nim = []
    list_nama = []
    list_tugas = []
    list_uts = []
    list_uas = []
    list_nakhir = []
    list_grade = []
    minimum_nilai = 100
    maximum_nilai = 0
    index_min = 0
    index_max = 0
    total_nilai = 0

    n = int(input("Jumlah mahasiswa : "))
    for i in range(n):
        print ("\nInputkan Data ke-" + str(i+1))
        list_nim.append(int(input("NIM   : ")))
        list_nama.append(str(input("Nama  : ")))
        list_tugas.append(int(input("Tugas : ")))
        list_uts.append(int(input("UTS   : ")))
        list_uas.append(int(input("UAS   : ")))
        list_nakhir.append(30/100*(list_tugas[i]) + 30/100*(list_uts[i]) + 40/100*(list_uas[i]))
        
        grade = list_nakhir[i]
        if(grade>=85):
            list_grade.append("A")
        elif(grade >=80 and grade <85):
            list_grade.append("A-")
        elif(grade >=75 and grade <80):
            list_grade.append("B+")
        elif(grade >=70 and grade <75):
            list_grade.append("B")
        elif(grade >=65 and grade <70):
            list_grade.append("B-")
        elif(grade >=60 and grade <65):
            list_grade.append("C")
        elif(grade >=45 and grade <60):
            list_grade.append("D")
        else:
            list_grade.append("E")
        
        if minimum_nilai > grade:
            minimum_nilai = grade
            index_min = i
        if maximum_nilai < grade:
            maximum_nilai = grade
            index_max = i

        total_nilai += grade
    rata_rata = total_nilai/n

    print("\n\nLaporan Nilai Data Science")
    print("+====+================+===============================+=====+=====+=====+=======+=======+")
    print("| No | NIM            | Nama                          | TGS | UTS | UAS | Akhir | Grade |")
    print("+====+================+===============================+=====+=====+=====+=======+=======+")
    for x in range(n):
        print("| %-2d | %-11s    | %-14s                | %-3d | %-3d | %-3d | %-4.02f |   %s   |"%(x+1, list_nim[x], list_nama[x], list_tugas[x], list_uts[x], list_uas[x], list_nakhir[x], list_grade[x]))
    print("+====+================+===============================+=====+=====+=====+=======+=======+")

    print("\n")
    print("%-15s : %-3.02f"%("Total nilai", total_nilai))
    print("%-15s : %-3.02f"%("Nilai Rata-Rata", rata_rata))
    print("%-15s : %-3.02f, NIM : %s - Nama : %s"%("Nilai Terendah", minimum_nilai, list_nim[index_min], list_nama[index_min]))
    print("%-15s : %-3.02f, NIM : %s - Nama : %s"%("Nilai Tertinggi", maximum_nilai, list_nim[index_max], list_nama[index_max]))

if __name__ == "__main__":
    main()