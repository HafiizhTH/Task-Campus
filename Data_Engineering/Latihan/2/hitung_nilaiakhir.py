from input_nilai import uts,uas,quiz
from hitung_nilairatarata import hitungratarata

def nilai_akhir():
    n_akhir = (0.25 * hitungratarata()) + (0.05 * quiz) + (0.30 * uts) + (0.40 * uas)
    nakhir = '%.2f' % n_akhir
    nilai_akhir2 = float(nakhir)
    return nilai_akhir2
