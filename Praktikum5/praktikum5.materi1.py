# ==========================================
# CONTOH REKURSI 1 - FAKTORIAL
# ==========================================
# Nama    : Syahrul Hidayatullah
# NIM     : J0403251145
# Kelas   : A2
# ==========================================

def faktorial(n):
    # Base case:
    # Jika n = 0, faktorial bernilai 1
    # (0! = 1)
    if n == 0:
        return 1
    
    # Recursive case:
    # n! = n × (n-1)!
    return n * faktorial(n - 1)

print(faktorial(5))  # Output: 120


# ==========================================
# PENJELASAN SINGKAT
# ==========================================
# Alur faktorial(5):
# 5 × 4 × 3 × 2 × 1 × 1

# Proses rekursi:
# faktorial(5)
# = 5 * faktorial(4)
# = 5 * 4 * faktorial(3)
# ...
# sampai faktorial(0) → 1 (base case)

# Tanpa base case akan terjadi infinite recursion.
# ==========================================