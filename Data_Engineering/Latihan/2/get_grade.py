from hitung_nilaiakhir import nilai_akhir

def nilai_indeks():
    if(nilai_akhir() >= 85): grade = 'A'
    elif(nilai_akhir() >= 80): grade = 'A-'
    elif(nilai_akhir() >= 75): grade = 'B+'
    elif(nilai_akhir() >= 70): grade = 'B'
    elif(nilai_akhir() >= 65): grade = 'B-'
    elif(nilai_akhir() >= 60): grade = 'C'
    elif(nilai_akhir() >= 45): grade = 'D'
    else: grade = 'E'
    return grade