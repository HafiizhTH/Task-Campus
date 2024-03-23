import csv

def lihat():
   rows = []

   with open('data_kontak.csv', 'r') as csvfile:
      csvreader = csv.reader(csvfile)

      for row in rows:
        print(f"{row['NO']},{row['NAMA']},{row['TELEPON']}")
      
      rows = list(csvreader)
      print(rows)

def inputan():
   NO = []
   NAMA = []
   TELEPON = []

   with open('data_kontak.csv', mode='a',newline='') as csvfile:
        fieldnames = ['NO', 'NAMA', 'TELEPON']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        print("======== Modifikasi ========\n")
        n = int(input("Jumlah : "))
        
        for i in range(n):
         print ("\nInputkan Data ke-" + str(i+1))
         NO = input("NO   : ")
         NAMA = input("NAMA    : ")
         TELEPON = input("TELEPON : ")        
         print("\n============================\n")
         
         writer.writerow({'NO': NO, 'NAMA': NAMA, 'TELEPON': TELEPON})    

if __name__ == "__main__":
   inputan()
   lihat()