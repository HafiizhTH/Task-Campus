from input_nilai import n_tugas

def hitungratarata():
    total = sum(n_tugas)
    rata = '%.2f' % (total/len(n_tugas))
    rata2 = float(rata)
    return rata2
