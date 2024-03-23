import csv
import json
from os import system, name
import os.path

CSV_PATH = "2012500720.csv"
FIELDNAMES = ["nim", "nama", "alamat", "fakultas", "prodi", "jenjang", "kelas"]

datas = {}


def main():
    csv_to_json()
    while(1):
        print_menu()
        huruf = input("Input Huruf Menu: ")
        if huruf.lower() == "c": input_create_data()
        if huruf.lower() == "r": retrieve_data()
        if huruf.lower() == "u": input_update_data()
        if huruf.lower() == "d": input_delete_data()
        if huruf.lower() == "s": input_search_data()
        if huruf.lower() == "x": exit()

        input("Enter untuk ke menu utama")

def print_menu():
    clrscr()
    print("+=============================+")
    print(f"| NIM : 2012500720            |")
    print(f"| Nama: Budi Luhur             |")
    print("+-----------------------------+")
    print("| Menu                        |")
    print("| [C] Create                  |")
    print("| [R] Retrieve                |")
    print("| [U] Update                  |")
    print("| [D] Delete                  |")
    print("| [S] Search                  |")
    print("| [X] Exit                    |")
    print("+=============================+")
        


def csv_to_json():
    
    if not os.path.exists(CSV_PATH):
        insert_data()
    
    with open(CSV_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nim = row['nim']
            datas[nim] = {}
            datas[nim]['nama'] = row['nama']
            datas[nim]['alamat'] = row['alamat']
            datas[nim]['fakultas'] = row['fakultas']
            datas[nim]['prodi'] = row['prodi']
            datas[nim]['jenjang'] = row['jenjang']
            datas[nim]['kelas'] = row['kelas']
        

def clrscr():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

def create_data(nim, nama, alamat):
    digit_fakultas = nim[2:4]
    digit_prodi = nim[2:4]
    digit_jenjang = nim[4]
    digit_kelas = nim[5]

    tahun_masuk = nim[0:2] # ga tau buat apa wkwk
    fakultas = get_fakultas(digit_fakultas)
    prodi = get_prodi(digit_prodi)
    jenjang = get_jenjang(digit_jenjang)
    kelas = get_kelas(digit_kelas)

    datas[nim] = {}

    datas[nim]['nama'] = nama
    datas[nim]['alamat'] = alamat
    datas[nim]['fakultas'] = fakultas
    datas[nim]['prodi'] = prodi
    datas[nim]['jenjang'] = jenjang
    datas[nim]['kelas'] = kelas

def get_kelas(digit):
    if digit == "0": return "Reguler"
    if digit == "1":  return "Kry Pusat"
    if digit == "2": return "Kry Roxy"
    if digit == "3": return "Kry Salemba"

def get_jenjang(digit):
    if digit == "3": return "D3"
    if digit == "5": return "S1"
    if digit == "6": return "S2"

def get_prodi(digit):
    if digit == "11": return "TI"
    if digit == "12": return "SI"
    if digit == "13": return "SK"
    if digit == "21": return "SE"
    if digit == "31": return "MN"
    if digit == "32": return "AK"
    if digit == "42": return "HI"
    if digit == "43": return "KR"
    if digit == "51": return "AR"
    if digit == "52": return "EL"
    if digit == "71": return "IK"
    if digit == "72": return "DK"
    
def get_fakultas(digit):
    if digit == "11" or digit == "12" or digit == "13": return "FTI"
    if digit == "21": return "ASTRI"
    if digit == "31" or digit == "32": return "FEB"
    if digit == "42" or digit == "43": return "FISIP"
    if digit == "51" or digit == "52": return "FT"
    if digit == "71" or digit == "72": return "FKDK"

    insert_data()



def input_create_data():
    clrscr()
    print("+===============+")
    print("|Create Data    |")
    print("+===============+\n")
    nim = input("Input NIM: ")
    nama = input("Nama : ")
    alamat = input("Alamat : ")

    if len(nim) < 10 or len(nim) > 10:
        print("\nMaaf NIM harus 10 digit angka!")
        return
    if nim in datas.keys():
        print("\nData dengan NIM sama sudah ada!")
        return

    create_data(nim, nama, alamat)
    print("\nData berhasil dimasukkan!")



def retrieve_data():
    clrscr()
    show_data()

def show_data():
    print("%-11s%-8s%-11s%-9s%-6s%-8s%-8s"%("NIM", "NAMA", "ALAMAT", "FAKULTAS", "PRODI","JENJANG", "KELAS"))
    
    for k, v in datas.items():
        print("%-11s%-8s%-11s%-9s%-6s%-8s%-8s"%(k, v['nama'], v['alamat'], v['fakultas'], v['prodi'], v['jenjang'], v['kelas']))



def update_data(nim, nama, alamat):
    datas[nim]['nama'] = nama
    datas[nim]['alamat'] = alamat

    insert_data()

def input_update_data():
    clrscr()
    show_data()
    target_nim = input("Input NIM: ")
    if not target_nim in datas.keys():
        print("\nMaaf NIM tidak ada di database!")
        return

    nama_baru = input("Update Nama : ")
    alamat_baru = input("Update Alamat : ")

    update_data(target_nim, nama_baru, alamat_baru)
    
    print("\nData berhasil diupdate!")



def delete_data(nim):
    datas.pop(nim, None)

    insert_data()

def input_delete_data():
    clrscr()
    show_data()
    target_nim = input("Input NIM yang akan dihapus: ")
    if not target_nim in datas.keys():
        print("\nMaaf NIM tidak ada di database!")
        return

    delete_data(target_nim)

def search_data(nim):
    nama = datas[nim]['nama']
    alamat = datas[nim]['alamat']
    fakultas = datas[nim]['fakultas']
    prodi = datas[nim]['prodi']
    jenjang = datas[nim]['jenjang']
    kelas = datas[nim]['kelas']

    print(f"Ditemukan Hasil Pencarian NIM: {nim}")
    print(f"Nama : {nama}")
    print(f"Alamat : {alamat}")
    print(f"Fakultas : {fakultas}")
    print(f"Prodi : {prodi}")
    print(f"Jenjang : {jenjang}")
    print(f"Kelas : {kelas}")



def input_search_data():
    clrscr()
    target_nim = input("Input NIM yang akan dicari: ")
    
    if not target_nim in datas.keys():
        print(f"\nData tidak ditemukan untuk NIM: {target_nim}")
        return

    search_data(target_nim)



def insert_data():
    with open(CSV_PATH, 'w', newline = '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        for k, v in datas.items():
            writer.writerow({"nim": k, "nama": v['nama'],"alamat": v['alamat'], "fakultas" : v['fakultas'], "prodi" : v['prodi'], "jenjang" : v['jenjang'], "kelas" : v['kelas']})



if __name__ == "__main__":
    main()
