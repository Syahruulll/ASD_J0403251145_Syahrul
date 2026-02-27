# ==========================================
# PRAKTIKUM 5 - LATIHAN 3
# ==========================================
# Nama    : Syahrul Hidayatullah
# NIM     : J0403251145
# Kelas   : A2
# ==========================================


# Fungsi rekursif untuk mencari nilai maksimum dalam list
def cari_maks(data, index=0):
    # Base case:
    # Jika index sudah di elemen terakhir,
    # maka kembalikan nilai elemen tersebut
    if index == len(data) - 1:
        return data[index]
    
    # Recursive call:
    # Mencari nilai maksimum dari sisa list
    maks_sisa = cari_maks(data, index + 1)
    
    # Membandingkan nilai sekarang dengan hasil rekursi
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa


# Data dan pemanggilan fungsi
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))


# ==========================================
# PENJELASAN SINGKAT
# ==========================================

# Base case terjadi saat index berada di elemen terakhir.
# Fungsi mengembalikan nilai elemen tersebut.

# Recursive call memanggil fungsi dengan index + 1
# untuk mencari maksimum dari sisa elemen.

# Alur:
# Fungsi berjalan sampai elemen terakhir (5),
# lalu membandingkan:
# 9 vs 5 -> 9
# 2 vs 9 -> 9
# 7 vs 9 -> 9
# 3 vs 9 -> 9

# Hasil akhirnya adalah 9.

# Rekursi bekerja dari belakang ke depan
# karena menggunakan sistem stack (LIFO).
# ==========================================