
#Superclass
class pegawai:
    def __init__(self, Idnumber, nama, telepon, departemen):
        self.Idnumber = Idnumber
        self.nama = nama
        self.telepon = telepon
        self.departemen = departemen

#Subclass
class pegawai_tetap(pegawai):
    def __init__(self, Idnumber, nama, telepon, departemen, gaji_pokok, uangmakan, uangtransport):
        pegawai.__init__(self, Idnumber, nama, telepon, departemen)
        self.gaji_pokok = gaji_pokok
        self.uangmakan = uangmakan
        self.uangtransport = uangtransport

    def Tampil_gaji(self):
        self.jumlah_gaji = self.gaji_pokok + self.uangmakan + self.uangtransport
        print("Jumlah Gaji    : ", self.jumlah_gaji)

    def Tampil_info(self):
        print("==================================")
        print("\tPegawai Tetap")
        print("==================================")
        print("Id Number      : ", self.Idnumber)
        print("Nama           : ", self.nama)
        print("telepon        : ", self.telepon)
        print("departemen     : ", self.departemen)
        print("Gaji Pokok     : ", self.gaji_pokok)
        print("Uang Makan     : ", self.uangmakan)
        print("Uang Transport : ", self.uangtransport)
    
class pegawai_honorer(pegawai):
    def __init__(self, Idnumber, nama, telepon, departemen, honor):
        pegawai.__init__(self, Idnumber, nama, telepon, departemen)
        self.honor = honor

    def Tampil_incentif(self):
        self.jumlah_incentif = self.honor
        print("Jumlah Incentif: ", self.jumlah_incentif)

    def Tampil_info(self):
        print("\n\n==================================")
        print("\tPegawai Honorer")
        print("==================================")
        print("Id Number      : ", self.Idnumber)
        print("Nama           : ", self.nama)
        print("telepon        : ", self.telepon)
        print("departemen     : ", self.departemen)
        print("Honorer        : ", self.honor)

a = pegawai_tetap(123, "Hafiizh", "082877262524", "Bank", 2000000, 1000000, 500000)
a.Tampil_info()
a.Tampil_gaji()

b = pegawai_honorer(345, "tukul", "08764543455", "CEO", 5000000)
b.Tampil_info()
b.Tampil_incentif()

