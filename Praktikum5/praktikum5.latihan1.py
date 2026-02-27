# ==========================================
# PRAKTIKUM 5 - LATIHAN 1
# ==========================================
# Nama    : Syahrul Hidayatullah
# NIM     : J0403251145
# Kelas   : A2
# ==========================================

# Fungsi rekursif menghitung pangkat
def pangkat(a, n):
    # Base case: jika n = 0 maka hasilnya 1
    if n == 0:
        return 1
    
    # Recursive case: a^n = a * a^(n-1)
    return a * pangkat(a, n - 1)

# Pemanggilan fungsi
print(pangkat(2, 4))  # Output: 16


# ==========================================
# PENJELASAN SINGKAT
# ==========================================

# Base case menghentikan rekursi saat n = 0.
# Recursive call memanggil fungsi sendiri dengan n-1.
# Alur: 2^4 = 2 * 2 * 2 * 2 * 1 = 16.
# Tanpa base case akan terjadi infinite recursion.
# ==========================================