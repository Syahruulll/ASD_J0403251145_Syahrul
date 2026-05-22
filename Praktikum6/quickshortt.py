def quick_sort(arr):

    # jika jumlah data 1 atau kosong
    # maka langsung dikembalikan
    if len(arr) <= 1:
        return arr
    
    # menentukan pivot (ambil elemen terakhir)
    pivot = arr[-1]

    kiri = []
    kanan = []

    # membandingkan setiap elemen dengan pivot
    for i in range(len(arr)-1):

        if arr[i] < pivot:
            kiri.append(arr[i])   # masuk ke kiri
        else:
            kanan.append(arr[i])  # masuk ke kanan

    # rekursi
    return quick_sort(kiri) + [pivot] + quick_sort(kanan)


# data contoh
data_angka = [9, 4, 7, 3, 10, 5, 1]

print("Data sebelum diurutkan : ", data_angka)

hasil = quick_sort(data_angka)

print("Data setelah diurutkan : ", hasil)
