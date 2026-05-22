# ======================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Syahrul Hidayatullah
# NIM     : J0403251145
# Kelas   : TPL A2
# ======================================================================

# 1. FILE HANDLING & DICTIONARY
def muat_data_buku(nama_file='buku.txt'):
    """
    Membaca file buku.txt dan menyimpan data ke dictionary.
    Format file: kode_buku,judul,harga
    """
    try:
        db = {}
        with open(nama_file, encoding='utf-8') as f:
            for line in f:
                kode, judul, harga = line.strip().split(',')
                db[kode] = {'judul': judul, 'harga': int(harga)}  # Simpan ke dict
        print("Data buku berhasil dimuat.")
        return db
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
        return {}
    except Exception as e:
        print(f"Error membaca file: {e}")
        return {}

# 2. LINKED LIST - MANAJEMEN PROMOSI
class Node:
    """Node untuk menyimpan data buku promosi."""
    def __init__(self, judul):
        self.judul = judul
        self.next = None

class LinkedListPromosi:
    """Linked List untuk mengelola daftar buku promosi."""
    def __init__(self):
        self.head = None

    def tambah_buku_promosi(self, judul):
        """
        Menambahkan buku ke daftar promosi.
        Jika list kosong, node baru jadi head.
        """
        baru = Node(judul)
        if not self.head:
            self.head = baru
        else:
            cur = self.head
            while cur.next:  # Cari node terakhir
                cur = cur.next
            cur.next = baru

        # Simpan buku promosi ke file
        try:
            with open("buku.txt", "a", encoding="utf-8") as f:
                f.write(f"PROMO,{judul},0\n")  # Harga 0 untuk promosi
            print(f"Buku '{judul}' ditambahkan ke promosi dan disimpan.")
        except Exception as e:
            print(f"Error menyimpan buku promosi: {e}")

    def tampilkan_promosi(self):
        """
        Menampilkan semua buku dalam daftar promosi.
        Jika kosong, tampilkan pesan.
        """
        cur = self.head
        if not cur:
            print("Daftar promosi kosong.")
            return
        i = 1
        while cur:
            print(f"{i}. {cur.judul}")
            cur = cur.next
            i += 1

# 3. QUEUE - ANTREAN KASIR
class AntreanKasir:
    """Queue untuk mengelola antrean pelanggan di kasir."""
    def __init__(self):
        self.antrean = []

    def tambah_antrean(self, nama_pelanggan):
        """
        Menambahkan pelanggan ke antrean (enqueue).
        """
        self.antrean.append(nama_pelanggan)
        print(f"{nama_pelanggan} ditambahkan ke antrean.")

    def layani_pelanggan(self):
        """
        Melayani pelanggan pertama di antrean (dequeue).
        Jika antrean kosong, tampilkan pesan.
        """
        if not self.antrean:
            print("Tidak ada pelanggan dalam antrean.")
        else:
            print(f"Melayani pelanggan: {self.antrean.pop(0)}")

# 4. SORTING - LAPORAN TRANSAKSI
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga menggunakan Insertion Sort.
    """
    for i in range(1, len(list_harga)):
        key = list_harga[i]
        j = i - 1
        while j >= 0 and list_harga[j] > key:
            list_harga[j + 1] = list_harga[j]
            j -= 1
        list_harga[j + 1] = key
    return list_harga

# ======================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ======================================================================
def main():
    # Inisialisasi data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        # Tampilkan menu utama
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            # Menu 1: Lihat katalog buku
            print("\nKatalog Buku:")
            if not data_buku:
                print("Katalog kosong atau file tidak ditemukan.")
            else:
                for kode, info in data_buku.items():
                    print(f"{kode}: {info['judul']} - Rp{info['harga']}")
        elif pilihan == '2':
            # Menu 2: Kelola daftar promosi
            print("\n--- Kelola Daftar Promosi ---")
            print("1. Tambah Buku Promosi")
            print("2. Tampilkan Daftar Promosi")
            sub_pilihan = input("Pilih menu (1-2): ")

            if sub_pilihan == '1':
                judul_baru = input("Masukkan judul buku untuk promosi: ")
                list_promosi.tambah_buku_promosi(judul_baru)
            elif sub_pilihan == '2':
                print("\nDaftar Buku Promosi:")
                list_promosi.tampilkan_promosi()
            else:
                print("Pilihan tidak valid!")
        elif pilihan == '3':
            # Menu 3: Kelola antrean kasir
            print("\n--- Kelola Antrean Kasir ---")
            print("1. Tambah Pelanggan ke Antrean")
            print("2. Layani Pelanggan")
            sub_pilihan = input("Pilih menu (1-2): ")

            if sub_pilihan == '1':
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama)
            elif sub_pilihan == '2':
                antrean_toko.layani_pelanggan()
            else:
                print("Pilihan tidak valid!")
        elif pilihan == '4':
            # Menu 4: Lihat laporan penjualan terurut
            print("\nLaporan Penjualan Terurut:")
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            print("Harga Sesudah Urut:", hasil_sort)
        elif pilihan == '5':
            # Menu 5: Keluar
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program utama
if __name__ == "__main__":
    main()