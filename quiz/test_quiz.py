from index import muat_data_buku, LinkedListPromosi, AntreanKasir, urutkan_transaksi

def run_tests():
    print("== Muat Data Buku ==")
    db = muat_data_buku('buku.txt')
    print(db)

    print('\n== LinkedList Promosi ==')
    lp = LinkedListPromosi()
    lp.tambah_buku_promosi('Dasar Pemrograman')
    lp.tambah_buku_promosi('Pemrograman Python Lanjut')
    lp.tampilkan_promosi()

    print('\n== Antrean Kasir ==')
    q = AntreanKasir()
    q.tambah_antrean('Alice')
    q.tambah_antrean('Bob')
    q.layani_pelanggan()
    q.layani_pelanggan()
    q.layani_pelanggan()

    print('\n== Urutkan Transaksi ==')
    transaksi = [150000, 50000, 200000, 75000, 120000]
    print('Sebelum:', transaksi)
    print('Sesudah:', urutkan_transaksi(transaksi))

if __name__ == '__main__':
    run_tests()
