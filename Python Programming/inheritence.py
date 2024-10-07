# membuat kelas induk bernama hewan
class hewan:
    # membuat method __init__ untuk menginisialisasi objek
    def __init__(self, nama, jenis):
        # membuat instance attribute bernama nama dan jenis
        self.nama = nama
        self.jenis = jenis
    
    # membuat instance method
    def bersuara(self):
        # menampilkan suara hewan
        print(f"{self.nama} bersuara")
        
# membuat kelas anak bernama kucing yang mewarisi dari kelas hewan
class kucing(hewan):
    # membuat method __init__ untuk menginisialisasi objek
    def __init__(self, nama, jenis, warna):
        # memanggil method __init__ dari kelas induk dengan parameter nama dan jenis
        super().__init__(nama, jenis)
        # membuat instance attribute tambahan bernama warna
        self.warna = warna
        
    # menimpa (overwrite) instance method bersuara dari induk
    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara meong")
        
# membuat objek bernama hewan1 dri kelas hewan dengan parameter "lion" dan "mamalia"
hewan1 = hewan("Lion", "Mamalia")
# membuat objek bernama kucing1 dari kelas kcuing dengan parameter "kitty", "mamalia", dan "putih"
kucing1 = kucing("Moca", "Mamalia", "Putih")

# memanggil instance method bersuara dari objek hewan1 dan kucing1 
hewan1.bersuara()
kucing1.bersuara()

# mengakses instance attribute nama, jensi, dan warna dari objek hewan1 dan kucing1
print(hewan1.nama)
print(hewan1.jenis)
print(kucing1.nama)
print(kucing1.jenis)
print(kucing1.warna)
