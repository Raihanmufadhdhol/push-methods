# mengimport modul threading
import threading
# mengimport modul time untuk menambahkan delay
import time

# membuat fungsi bernama print_nama yang menerima paramter nama
def print_nama(nama):
    # menampilkan nama yang diberikan sebagai parameter
    print(f"Halo, Nama saya {nama}")
    # menambahkan delay selama 2 detik
    time.sleep(1)
    # menampillkan pesan selesai
    print(f"Selesai menampilkan nama {nama}")
    
# membuat objek thread bernama t1 dengan target fungsi print_nama dan args "Budi"
t1 = threading.Thread(target=print_nama, args=("Budi",))
# membuat objek thread bernama t2 dengan target fungsi print_nama dan args "Ani"
t2 = threading.Thread(target=print_nama, args=("Ani",))

# type: ignore 
# memulai eksekusi thread t1 dan t2 secara bersamaan
t1.start()
t2.start()

#menunggu thread t1 dan t2 selesai sebelum melankutkan kode selanjutnya
t1.join()
t2.join()

# menampilkan pesan akhir
print("Semua thread selesai")