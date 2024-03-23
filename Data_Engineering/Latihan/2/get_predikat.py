from hitung_nilaiakhir import nilai_akhir

def predikat():
    if(nilai_akhir() >= 85): predikat = 'SANGAT BAIK'
    elif(nilai_akhir() >= 80): predikat = 'BAIK'
    elif(nilai_akhir() >= 75): predikat = 'CUKUP BAIK'
    elif(nilai_akhir() >= 70): predikat = 'CUKUP'
    elif(nilai_akhir() >= 65): predikat = 'BELUM CUKUP'
    elif(nilai_akhir() >= 60): predikat = 'KURANG'
    else: predikat = 'SANGAT KURANG'
    return predikat
