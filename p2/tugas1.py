nama_file = "stok_barang.txt"

def baca_data(nama_file):
    data_dict = {}
    with open(nama_file,"r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            if not baris: continue
            
            kode_barang, nama_barang, stok_barang = baris.split(",")
            data_dict[kode_barang] ={
                "nama_barang": nama_barang,
                "stok_barang": int(stok_barang)
            }
        return data_dict
buka_data = baca_data(nama_file)
print("jumlah data terbaca", len(buka_data))
print(buka_data     )
 
    