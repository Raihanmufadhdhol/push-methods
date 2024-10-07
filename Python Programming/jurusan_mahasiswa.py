# membuat kelas bernama mahasiswa
class mahasiswa:    
    # membuat method __init__ untuk menginisialisasi objek
    def __init__(self, nama, nim, jurusan):
        #membuat instance atribut bernama nama dan nim
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        
    # mengakses instance method bernama perkenalan
    def perkenalan(self):
        # mengakses instance attribute nama dan nim dari objek
        print(f"Halo, Nama saya {self.nama}, nim saya {self.nim}, saya berasal dari jurusan {self.jurusan}")
        
    @classmethod # ini adalah dekorator, class methode tidak dapat mengakses insstance atribut
    def ganti_jurusan(cls, jurusan_baru):
        # mengubah nilai class attribute jurusan dari kelas
        cls.jurusan = jurusan_baru # ini tidak bakal ada yg berubah soalnya instance atribut gabisa diambil dari objek, bisanya variabel bebas
        
    # membuat static methode bernama hitung_ipk
    @staticmethod # ini adalah dekorator,
    def hitung_ipk(nilai):
        # menghitung ipk dari nilai yang diberikan sebagai parameter
        total = 0
        for n in nilai:
            total += n
        ipk = total / len(nilai)
        return ipk

# membuat objek bernama mhs1 dan mhs2 dari kelas Mahasiswa
mhs1 = mahasiswa("Budi", "1029371864", "Cyber Security")
mhs2 = mahasiswa("Davin", "139271097", "AI Engineer")

ipk_mhs1 = mahasiswa.hitung_ipk([80, 92, 90, 75, 85])
ipk_mhs2 = mahasiswa.hitung_ipk([87, 90, 85, 80, 95])

# mengakses class atribut bernama mhs1 dan mhs2 dari kelas mahasiswa
print(mhs1.jurusan) # outputnya bakal data engineer
print(mhs2.jurusan) # outputnya bakal data engineer
print(mhs1.nama)
print(mhs1.nim)
print(mhs2.nama)
print(mhs2.nim)

mhs1.perkenalan()
mhs2.perkenalan()

# mengubah nilai class atribut jurusan dari objek mhs1
# mhs1.jurusan = "Data Science"
# mhs2.jurusan = "Data Analyst"

mahasiswa.ganti_jurusan("IT Support")

mhs1.perkenalan()
mhs2.perkenalan()

print(f"IPK dari {mhs1.nama} adalah {ipk_mhs1}")
print(f"IPK dari {mhs2.nama} adalah {ipk_mhs2}")

#mengubah nilai instance attribute nama dan nim dari objek mhs1
mhs1.nama = "Rudi"
mhs1.nim = "1531513"

# mengakses class atribut jurusan dari objek mhs1 dan mhs2 setelah diubah
print(mhs1.jurusan)
print(mhs2.jurusan)
print(mhs1.nama)
print(mhs1.nim)
print(mhs2.nama)
print(mhs2.nim)

