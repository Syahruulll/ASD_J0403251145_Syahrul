# ==========================================================
# Praktikum 2: ADT & File Handling (Studi Kasus: Data Mahasiswa)
# Latihan 1: membuat fungsi load data dari file
# Nama : Syahrul Hidayatullah
# NIM  : J0403251145
# Kelas : TPL A2
# ==========================================================


#variable menyimpan file
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {}
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
    
                
                nim, nama, nilai = baris.split(",")
                data_dict[nim] = {
                    "nama": nama,
                    "nilai": int(nilai)
                }
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan. Memulai dengan data kosong.")
    return data_dict
    
    
buka_data = baca_data(nama_file)
# print("jumlah data terbaca", len(buka_data))


# ==========================================================
# Praktikum 2: ADT & File Handling (Studi Kasus: Data Mahasiswa)
# Latihan 2: membuat fungsi menampilkan data
# ==========================================================

def tampilkan_data(data_dict):
    #membuat header table
    print("\n===== DAFTAR MAHASISWA =====")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':>5}")
    '''Untuk tampilan yang rapi, atur f-string formatting.
        {nim:<10} artinya:
        tampilkan nim < = rata kiri dengan 10 = lebar kolom 10 karakter
        {nama:<12} artinya:
        tampilkan nama rata kiri. lebar kolom 12 karakter
        {nilai:>5} artinya:
        tampilkan nilai > = rata kanan, lebar kolom 5 karakter (biar angka sejajar)
    '''
    print("-" * 35) #buat garis header tabel
    
    #Pengulangan untuk mencetak data
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {int(nilai):>5}")
    
# tampilkan_data(buka_data) #memanggil fungsi untuk menampilkan data


# ==========================================================
# Praktikum 2: ADT & File Handling (Studi Kasus: Data Mahasiswa)
# Latihan 3: membuat fungsi mencari data
# ==========================================================

#membuat fungsi mencari data
def cari_mahasiswa(data_dict):
    #Mencari mahasiswa berdasarkan NIM (key dictionary).
    #membuat input nim mahasiswa yag akan dicari
    nim_cari = input("Masukkan NIM yang ingin dicari (contoh: J0403001): ").strip()
    
    
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        
        print("\n=== Data Mahasiswa Ditemukan ===")
        print(f"NIM : {nim_cari}")
        print(f"Nama : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("\nData tidak ditemukan. Pastikan NIM yang dimasukkan benar.")
        
# ==========================================================
# Praktikum 2: ADT & File Handling (Studi Kasus: Data Mahasiswa)
# Latihan 4: membuat fungsi update data
# ==========================================================

# def update_nilai_mahasiswa(data_dict):
    #awali dulu dengan mencarii nimm/ data mahasiswa yang ingin diubah
    # nim = input("Masukkan NIM yang ingin diupdate nilainya: ").strip()
    
    # if nim not in data_dict:
    #    print("NIM tidak ditemukan. Update dibatalkan.")
    # nilai_lama = data_dict[nim]["nilai"]

def update_nilai_mahasiswa(data_dict):
    """
    Mengubah nilai mahasiswa berdasarkan NIM.
    Aturan:
    - NIM harus ada
    - Nilai baru harus 0–100
    """
    nim = input("Masukkan NIM yang ingin diupdate nilainya: ").strip()
    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan.")

        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan.")
        return
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update dibatalkan.")
        return
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru
    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}.")
    
# ubah_data(buka_data)


# # --- Program utama Latihan 4 ---
# update_nilai_mahasiswa(data_mahasiswa)
# # Menampilkan ulang tabel untuk memastikan data berubah
# tampilkan_semua_mahasiswa(data_mahasiswa)



# ==========================================================
# Praktikum 2: ADT & File Handling (Studi Kasus: Data Mahasiswa)
# Latihan 5: membuat fungsi menyimpan data pada file
# ==========================================================

#membuat fungsi menyimpan data ke file
def simpan_data_mahasiswa(nama_file, data_dict):
    """
    Menyimpan data mahasiswa dari dictionary ke file.
    Format per baris: NIM,NAMA,NILAI
    """
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#memnaggil fungsi ke simpan data
# simpan_data_mahasiswa(nama_file, buka_data)
# print("\n Data berhasil disimpan ke file: ", nama_file)



# ==========================================================
# Praktikum 2: ADT & File Handling (Studi Kasus: Data Mahasiswa)
# Latihan 6: membuat menu interaktif
# ==========================================================


def main():
    buka_data = baca_data(nama_file) 
    
    while True:
        print("\n=== MENU DATA MAHASISWA ===")
        print("1. Tampilkan semua data")
        print("2. Cari data berdasarkan NIM")
        print("3. Update nilai mahasiswa")
        print("4. Simpan data ke file")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_mahasiswa(buka_data)
        elif pilihan == "3":
            update_nilai_mahasiswa(buka_data)
        elif pilihan == "4":
            simpan_data_mahasiswa(nama_file, buka_data)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break # Break harus di dalam sini
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Harus di luar fungsi main (rata kiri)
if __name__ == "__main__":
    main()