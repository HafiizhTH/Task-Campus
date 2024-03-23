
#Superclass
class Customer:
    def __init__(self, Idnumber, nama, alamat, telepon):
        self.Idnumber = Idnumber
        self.nama = nama
        self.alamat = alamat
        self.telepon = telepon

#Subclass
class Member(Customer):
    def __init__(self, Idnumber, nama, alamat, telepon, Hrgmember, Diskon):
        Customer.__init__(self, Idnumber, nama, alamat, telepon)
        self.Hrgmember = Hrgmember
        self.Diskon = Diskon
    
    def Tampil_biaya(self):
        self.Diskon = self.Hrgmember * (self.Diskon/100)
        self.total_biaya =  self.Hrgmember - self.Diskon
        print("Total Biaya      : ", self.total_biaya)
    
    def Tampil_profil(self):
        print("\n\n==================================")
        print("\tMember")
        print("==================================")
        print("Id Number        : ", self.Idnumber)
        print("Nama             : ", self.nama)
        print("Alamat           : ", self.alamat)
        print("Telepon          : ", self.telepon)
        print("Harga Member     : ", self.Hrgmember)
        print("Diskon           : ", self.Diskon)

class NonMember(Customer):
    def __init__(self,  Idnumber, nama, alamat, telepon, Hrgnonmember):
        Customer.__init__(self, Idnumber, nama, alamat, telepon)
        self.Hrgnonmember = Hrgnonmember

    def Tampil_biaya(self):
        self.total_biaya =  self.Hrgnonmember
        print("Total Biaya      : ", self.total_biaya)

    def Tampil_profil(self):
        print("\n\n==================================")
        print("\tNon Member")
        print("==================================")
        print("Id Number        : ", self.Idnumber)
        print("Nama             : ", self.nama)
        print("Alamat           : ", self.alamat)
        print("Telepon          : ", self.telepon)
        print("Harga Non Member : ", self.Hrgnonmember)

Idnumber = int(input("Idnumber \t: "))
nama = str(input("Nama \t\t: "))
alamat = str(input("Alamat \t\t: "))
telepon = str(input("Telepon \t: "))
Hrgmember = int(input("Harga Member \t: "))
Diskon = int(input("Diskon \t\t: "))
Hrgnonmember = int(input("Harga Non Member \t: "))

a = Member(Idnumber, nama, alamat, telepon, Hrgmember, Diskon)
a.Tampil_profil()
a.Tampil_biaya()

b = NonMember(Idnumber, nama, alamat, telepon, Hrgnonmember)
b.Tampil_profil()
b.Tampil_biaya()