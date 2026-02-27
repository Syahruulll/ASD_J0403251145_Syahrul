# ==========================================
# PRAKTIKUM 5 - LATIHAN 5
# ==========================================
# Nama    : Syahrul Hidayatullah
# NIM     : J0403251145
# Kelas   : A2
# ==========================================


# Fungsi untuk menghasilkan semua kemungkinan PIN
def buat_pin(panjang, hasil=""):
    # Base case:
    # Jika panjang PIN sudah sesuai, cetak hasil
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    # Choose & Explore:
    # Loop angka 0 sampai 2
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)


# Pemanggilan fungsi
buat_pin(3)


# ==========================================
# PENJELASAN SINGKAT
# ==========================================
# Setiap digit memiliki 3 pilihan (0,1,2).
# Karena panjang 3 digit, maka jumlah kombinasi:
# 3^3 = 27 kemungkinan PIN.

# Cara mencegah angka yang sama muncul berulang:
# Kita bisa menambahkan pengecekan sebelum rekursi,
# misalnya:
#
# if angka not in hasil:
#     buat_pin(panjang, hasil + angka)

# Dengan begitu, satu angka tidak bisa dipakai
# lebih dari satu kali dalam satu PIN.
#
# Contoh hasil tanpa angka berulang:
# 012
# 021
# 102
# 120
# 201
# 210

# Teknik ini disebut pembatasan (constraint)
# dalam backtracking.
# ==========================================