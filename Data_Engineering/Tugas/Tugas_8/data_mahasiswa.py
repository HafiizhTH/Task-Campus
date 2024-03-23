import os

def main():
    file = open("data_mahasiswa.txt", "r")
    print(file.read())

def inputan():
    file = open("data_mahasiswa.txt", "a")

    print("\n======== Modifikasi ========\n")
    NO = input("NO   : ")
    NAMA = input("NAMA : ")
    NIM = input("NIM  : ")        
    print("\n============================\n")

    teks = "\n{} {} {}".format(NO, NAMA, NIM)
    file.write(teks)

    file.close()

def ubah_nama():
    os.rename("data_mahasiswa.txt", "mahasiswa_reguler.txt")

if __name__ == "__main__":
    main()
    inputan()
    ubah_nama()
