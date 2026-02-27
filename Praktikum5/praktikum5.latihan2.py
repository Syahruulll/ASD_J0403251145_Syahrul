# ==========================================
# PRAKTIKUM 5 - LATIHAN 2
# ==========================================
# Nama    : Syahrul Hidayatullah
# NIM     : J0403251145
# Kelas   : A2
# ==========================================

# Fungsi countdown untuk melihat alur masuk dan keluar rekursi
def countdown(n):
    # Base case
    if n == 0:
        print("Selesai")
        return
    
    # Proses sebelum rekursi (masuk)
    print("Masuk:", n)
    
    # Recursive call
    countdown(n - 1)
    
    # Proses setelah rekursi (keluar)
    print("Keluar:", n)


# Pemanggilan fungsi
countdown(3)


