
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
        print("\t    Member")
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
        print("\t   Non Member")
        print("==================================")
        print("Id Number        : ", self.Idnumber)
        print("Nama             : ", self.nama)
        print("Alamat           : ", self.alamat)
        print("Telepon          : ", self.telepon)
        print("Harga Non Member : ", self.Hrgnonmember)

a = Member(123, "Hafiizh", "Jakarta", "08826326383", 200000, 50)
a.Tampil_profil()
a.Tampil_biaya()

b = NonMember(345, "tukul", "Tangerang", "085772536647", 200000)
b.Tampil_profil()
b.Tampil_biaya()