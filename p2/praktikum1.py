# ==========================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 1A: Membaca seluruh isi file
# Nama : Syahrul Hidayatullah
# NIM  : J0403251145
# Kelas : TPL A2
# ==========================================================
# Membuka file dalam mode read ("r")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() # Membaca seluruh isi file sebagai string
# Menampilkan isi file ke layar
print("=== Isi File Data Mahasiswa ===")
print(isi_file)


with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
     baris = baris.strip() # Menghapus karakter newline
print(baris)


# ==========================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 1C: Analisis read() vs baca per baris
# ==========================================================
# -------------------------------
# Bagian A: Baca file dengan read()
# -------------------------------
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() # seluruh isi file jadi 1 string besar
print("=== HASIL READ() ===")
print("Tipe data:", type(isi_file))
print("Jumlah karakter:", len(isi_file))
print("Jumlah baris:", isi_file.count("\n") + 1)
# -------------------------------
# Bagian B: Baca file per baris
# -------------------------------
jumlah_baris = 0
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
baris = baris.strip()
print("Baris ke-", jumlah_baris)
print("Isinya :", baris)

# ==========================================================
# Latihan Dasar 2: Parsing baris menjadi kolom (split)
# ==========================================================
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
nim, nama, nilai = baris.split(",") # parsing 3 kolom
print("NIM:", nim, "| Nama:", nama, "| Nilai:", nilai)


# ==========================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 3: Membaca file dan menyimpan ke struktur data List
# ==========================================================
data_list = [] # List untuk menampung data mahasiswa
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
# Jika baris kosong, lewati
        if baris == "":
            continue
# Pecah data berdasarkan koma
nim, nama, nilai = baris.split(",")
# Simpan sebagai list kecil: [nim, nama, nilai]
data_list.append([nim, nama, int(nilai)])
print("=== Data Mahasiswa dalam List ===")
print(data_list)
print("=== Jumlah Record dalam List ===")
print("Jumlah record:", len(data_list))
print("=== Menampilkan Data Record Tertentu ===")
print("Contoh record pertama:", data_list[0])


# ==========================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 4A: Membaca file dan menyimpan ke struktur data Dictionary
# ==========================================================
data_dict = {} # Dictionary: key = NIM, value = data mahasiswa
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
# Jika baris kosong, lewati
        if baris == "":
            continue
nim, nama, nilai = baris.split(",")
# Simpan data mahasiswa dengan key NIM
data_dict[nim] = {
"nama": nama,
"nilai": int(nilai)
}
print("=== Data Mahasiswa dalam Dictionary ===")
print(data_dict)