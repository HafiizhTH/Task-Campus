from pendaftaran import nim

def kelas():
    if(nim[5] == '0'): kelas = "Kelas Regular"
    elif(nim[5] == '1'): kelas = "Kelas Sore"
    else : kelas = "Kelas Tidak Diketahui"
    return kelas