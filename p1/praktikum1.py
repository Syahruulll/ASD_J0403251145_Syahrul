#===============================================#
# Praktikum 1: konsep file ADT dan file handling
# Latihan Dasar 1: Membaca seluruh isi file data
#===============================================#

print("=== Membuka file dalam satu string ===")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
    print(isi_file)
    print("Tipe Data :", type(isi_file))


print("==== membuka file per baris ====")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris += 1
        baris = baris.strip()
        print("Baris ke-", jumlah_baris)
        print("Isinya :", baris)

#===============================================#
# Praktikum 1: konsep file ADT dan file handling
# Latihan Dasar 2: Parsing data per kolom
#===============================================#

print("==== Parsing data ====")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai)

#===============================================#
# Praktikum 1: konsep file ADT dan file handling
# Latihan Dasar 3: Menyimpan ke dalam LIST
#===============================================#

data_list = []

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_list.append([nim, nama, int(nilai)])

print("=== Menampilkan list ===")
print(data_list)
print("Contoh record ke-1:", data_list[0])
print("Contoh record ke-2:", data_list[1])
print("Jumlah record:", len(data_list))

#===============================================#
# Praktikum 1: konsep file ADT dan file handling
# Latihan Dasar 4: Menyimpan ke dalam DICTIONARY
#===============================================#

data_dict = {}

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
        }

print("=== Menampilkan Data Dictionary ===")
print(data_dict)
