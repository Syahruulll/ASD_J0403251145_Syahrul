# ==========================================
# CONTOH REKURSI 2 - TRACING MASUK/KELUAR
# ==========================================
# Nama    : Syahrul Hidayatullah
# NIM     : J0403251145
# Kelas   : A2
# ==========================================

def hitung(n):
    # Base case:
    # Jika n = 0, rekursi berhenti
    if n == 0:
        print("Selesai")
        return
    
    # Fase stacking (masuk ke stack)
    print("Masuk:", n)
    
    # Pemanggilan rekursif
    hitung(n - 1)
    
    # Fase unwinding (keluar dari stack)
    print("Keluar:", n)

hitung(3)


# ==========================================
# PENJELASAN SINGKAT
# ==========================================

# Output:
# Masuk: 3
# Masuk: 2
# Masuk: 1
# Selesai
# Keluar: 1
# Keluar: 2
# Keluar: 3

# "Masuk" terjadi saat fungsi dipanggil (stacking).
# "Keluar" terjadi setelah base case tercapai
# dan fungsi selesai satu per satu (unwinding).

# Karena menggunakan sistem stack (LIFO),
# urutan keluar menjadi terbalik.
# ==========================================