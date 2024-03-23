print("+====================================================+")
print("|  Program untuk mencetak informasi nilai mahasiswa  |")
print("+====================================================+")
print("| NIM    : 2012500720                                |")
print("| NAMA   : Hafiizh Taufiqul Hakim                    |")
print("+====================================================+\n")

from get_kelas import kelas
from get_jurusan import jurusan
from get_biaya import biaya

print("Jurusan : ", jurusan())
print("Kelas   : ", kelas())
print("Biaya   : ", biaya())