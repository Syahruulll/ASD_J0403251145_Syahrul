# ==========================================
# CONTOH BACKTRACKING 1 - KOMBINASI BINER
# ==========================================
# Nama    : Syahrul Hidayatullah
# NIM     : J0403251145
# Kelas   : A2
# ==========================================

def biner(n, hasil=""):
    # Base case:
    # Jika panjang string sudah sama dengan n,
    # maka cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # Choose + Explore: tambah '0'
    biner(n, hasil + "0")
    
    # Choose + Explore: tambah '1'
    biner(n, hasil + "1")

biner(3)


# ==========================================
# PENJELASAN SINGKAT
# ==========================================

# Setiap posisi memiliki 2 pilihan: 0 atau 1.
# Untuk n = 3, jumlah kombinasi = 2^3 = 8.

# Output:
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111

# Konsep:
# - Base case menghentikan saat panjang = n.
# - Choose + Explore mencoba semua kemungkinan.
# ==========================================