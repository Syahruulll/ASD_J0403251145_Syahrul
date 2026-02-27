# ==========================================
# CONTOH BACKTRACKING 2 - BINER DENGAN BATAS '1'
# ==========================================
# Nama    : Syahrul Hidayatullah
# NIM     : J0403251145
# Kelas   : A2
# ==========================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Pruning:
    # Jika jumlah '1' melebihi batas, hentikan cabang ini
    if jumlah_1 > batas:
        return
    
    # Base case:
    # Jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # Pilih '0' (jumlah_1 tetap)
    biner_batas(n, batas, hasil + "0", jumlah_1)
    
    # Pilih '1' (jumlah_1 bertambah 1)
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

biner_batas(4, 2)


# ==========================================
# PENJELASAN SINGKAT
# ==========================================

# Setiap posisi punya 2 pilihan: 0 atau 1.
# Tetapi jumlah '1' tidak boleh lebih dari batas.

# Pruning menghentikan rekursi lebih awal
# jika jumlah_1 > batas.

# Untuk n = 4 dan batas = 2:
# Kombinasi yang dicetak hanya yang
# memiliki maksimal 2 angka '1'.

# Teknik ini membuat pencarian lebih efisien
# karena cabang yang tidak memenuhi syarat
# langsung dihentikan.
# ==========================================