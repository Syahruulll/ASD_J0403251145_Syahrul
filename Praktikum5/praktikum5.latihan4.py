# ==========================================
# PRAKTIKUM 5 - LATIHAN 4
# ==========================================
# Nama    : Syahrul Hidayatullah
# NIM     : J0403251145
# Kelas   : A2
# ==========================================


# Fungsi untuk menghasilkan kombinasi huruf A dan B
def kombinasi(n, hasil=""):
    # Base case:
    # Jika panjang string sudah sama dengan n,
    # maka cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # Choose & Explore:
    # Tambah "A"
    kombinasi(n, hasil + "A")
    
    # Tambah "B"
    kombinasi(n, hasil + "B")


# Pemanggilan fungsi
kombinasi(2)


# ==========================================
# PENJELASAN SINGKAT
# ==========================================
# Konsep backtracking:
# - Choose  : pilih huruf (A atau B)
# - Explore : lanjutkan rekursi sampai panjang n
#
# Untuk n = 2, hasilnya:
# AA
# AB
# BA
# BB
#
# Jumlah kombinasi = 2^n
# Karena setiap posisi memiliki 2 pilihan (A atau B).
#
# Jika n = 2 -> 2^2 = 4 kombinasi
# Jika n = 3 -> 2^3 = 8 kombinasi
#
# Jadi semakin besar n, jumlah kombinasi
# bertambah secara eksponensial.
# ==========================================