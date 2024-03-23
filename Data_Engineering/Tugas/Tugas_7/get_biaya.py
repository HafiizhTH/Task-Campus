from pendaftaran import nim

def biaya():
    if(nim[3] == '1'): biaya = 9800000
    elif(nim[3] == '2'): biaya = 8500000
    elif(nim[3] == '3'): biaya = 9200000
    else : biaya = "Biaya Tidak Diketahui"
    return biaya