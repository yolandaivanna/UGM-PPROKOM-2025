from array import array

# Membuat list dan array
data_list = [100, 200, 300, 400]
data_array = array('i', [10, 20, 30, 40])

# Menambahkan elemen baru ke masing-masing
data_list.append(500)
data_array.append(50)

# Mengubah elemen pertama pada list menjadi string
data_list[0] = "Seratus"

# Menampilkan hasil
print("Isi data_list:", data_list)
print("Isi data_array:", data_array)

# Baris berikut jika dijalankan akan menyebabkan error
# data_array[0] = "Seratus"
