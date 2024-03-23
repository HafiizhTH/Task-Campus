
print("+====================================================+")
print("|  Program untuk mencetak informasi nilai mahasiswa  |")
print("+====================================================+")
print("| NIM    : 2012500720                                |")
print("| NAMA   : Hafiizh Taufiqul Hakim                    |")
print("+====================================================+\n")

from hitung_nilairatarata import hitungratarata
from hitung_nilaiakhir import nilai_akhir
from get_grade import nilai_indeks
from get_predikat import predikat


print("Rata-rata Nilai Tugas    :", hitungratarata())
print("Nilai Akhir              :", nilai_akhir())
print("Nilai Indeks             :", nilai_indeks())
print("Nilai Predikat           :", predikat())

