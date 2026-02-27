# ==========================================
# CONTOH REKURSI 3 - MENJUMLAHKAN ELEMEN LIST
# ==========================================
# Nama    : Syahrul Hidayatullah
# NIM     : J0403251145
# Kelas   : A2
# ==========================================

def jumlah_list(data, index=0):
    # Base case:
    # Jika index sama dengan panjang list,
    # berarti sudah tidak ada elemen lagi
    if index == len(data):
        return 0
    
    # Recursive case:
    # Elemen sekarang ditambah hasil rekursi
    return data[index] + jumlah_list(data, index + 1)

print(jumlah_list([2, 4, 6, 8]))  # Output: 20


# ==========================================
# PENJELASAN SINGKAT
# ==========================================

# Proses:
# 2 + 4 + 6 + 8 + 0

# Rekursi berjalan sampai index mencapai
# panjang list (base case → return 0).
# Setelah itu nilai dijumlahkan saat unwinding.

# Hasil akhir: 20
# ==========================================