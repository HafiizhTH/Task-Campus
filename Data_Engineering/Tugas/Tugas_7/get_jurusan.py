from pendaftaran import nim

def jurusan():
    if(nim[3] == '1'): jurusan = "Teknik Informatika"
    elif(nim[3] == '2'): jurusan = "Sistem Informasi"
    elif(nim[3] == '3'): jurusan = "Sistem Komputer"
    else : jurusan = "Jurusan Tidak Diketahui"
    return jurusan