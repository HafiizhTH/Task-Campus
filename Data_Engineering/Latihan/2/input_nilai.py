
uts = int(input("Masukan Nilai UTS        : "))
uas = int(input("Masukan Nilai UAS        : "))
quiz = int(input("Masukan Nilai QUIZ       : "))
b_tugas = int(input("Masukan Banyak Tugas     : "))

n_tugas = []
for i in range(b_tugas):
    ni = str(i+1)
    text = "Masukan Nilai Tugas ke-"+ni+" : "
    tugas = int(input(text))
    n_tugas.append(tugas)

