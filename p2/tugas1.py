# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Syahrul Hidayatullah
# NIM : J0403251145
# Kelas : TPL A2
# ==========================================================

nama_file = "stok_barang.txt"

#variable menyimpan file

def baca_data(nama_file):
    data_dict = {}
    with open(nama_file,"r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            if not baris:
                continue

            kode_barang, nama_barang, stok_barang = baris.split(",")
            data_dict[kode_barang] ={
                "nama_barang": nama_barang,
                "stok_barang": int(stok_barang)
            }
    return data_dict

# =========================
# membuat fungsi menampilkan data
# =========================
def tampilkan_data(data_dict):
    print("\nKODE BARANG | NAMA BARANG | STOK")
    print("-------------------------------------")
        #Pengulangan untuk mencetak data
    for kode_barang in sorted(data_dict.keys()):
        nama_barang = data_dict[kode_barang]["nama_barang"]
        stok_barang = data_dict[kode_barang]["stok_barang"]
        print(f"{kode_barang:<10} | {nama_barang:<12} | {stok_barang:>5}")

# =========================
# mencari barang
# =========================
def cari_barang(data_dict):
    cari_kode = input("Masukkan Kode Barang: ").strip()

    if cari_kode in data_dict:
        nama = data_dict[cari_kode]["nama_barang"]
        stok = data_dict[cari_kode]["stok_barang"]

        print("\n=== Data Barang Ditemukan ===")
        print(f"Kode barang : {cari_kode}")
        print(f"Nama        : {nama}")
        print(f"Stok        : {stok}")
    else:
        print("\nData tidak ditemukan.")

# =========================
# update stok barang
# =========================
def update_stok_barang(data_dict):
    kode_barang = input("Masukkan kode barang: ").strip()

    if kode_barang not in data_dict:
        print("Kode barang tidak ditemukan.")
        return

    try:
        stok_baru = int(input("Masukkan stok baru (0-100): "))
    except ValueError:
        print("Harus berupa angka!")
        return

    if stok_baru < 0 or stok_baru > 100:
        print("Stok harus antara 0–100.")
        return

    stok_lama = data_dict[kode_barang]["stok_barang"]
    data_dict[kode_barang]["stok_barang"] = stok_baru

    print(f"Stok {kode_barang} berubah dari {stok_lama} menjadi {stok_baru}.")

# =========================
# tambah barang
# =========================
def tambah_barang(data_dict):
    kode = input("Masukkan kode barang baru: ").strip()

    if kode in data_dict:
        print("Kode sudah ada!")
        return

    nama = input("Masukkan nama barang: ").strip()
    try:
        stok = int(input("Masukkan stok: "))
    except ValueError:
        print("Stok harus angka!")
        return

    data_dict[kode] = {
        "nama_barang": nama,
        "stok_barang": stok
    }

    print("Barang berhasil ditambahkan!")

# =========================
# hapus barang
# =========================
def hapus_barang(data_dict):
    kode = input("Masukkan kode barang yang ingin dihapus: ").strip()

    if kode in data_dict:
        del data_dict[kode]
        print("Barang berhasil dihapus!")
    else:
        print("Kode barang tidak ditemukan.")

# =========================
# simpan barang
# =========================
def simpan_data_barang(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode_barang in sorted(data_dict.keys()):
            nama = data_dict[kode_barang]["nama_barang"]
            stok = data_dict[kode_barang]["stok_barang"]
            file.write(f"{kode_barang},{nama},{stok}\n")

# =========================
# menu utama
# =========================
def main():
    buka_data = baca_data(nama_file)

    while True:
        print("\n=== MENU DATA BARANG ===")
        print("1. Tampilkan semua data")
        print("2. Cari data barang")
        print("3. Update stok barang")
        print("4. Tambah barang")
        print("5. Hapus barang")
        print("6. Simpan data ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_barang(buka_data)
        elif pilihan == "3":
            update_stok_barang(buka_data)
        elif pilihan == "4":
            tambah_barang(buka_data)
        elif pilihan == "5":
            hapus_barang(buka_data)
        elif pilihan == "6":
            simpan_data_barang(nama_file, buka_data)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
