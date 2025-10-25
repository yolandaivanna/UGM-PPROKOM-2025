# 1) Mengimpor modul array
import array

# 2) Membuat sebuah array integer dan mengisinya dengan 5 nilai angka bebas
angka = array.array('i', [10, 25, 30, 45, 50])

# 3) Menampilkan array tersebut beserta panjangnya (jumlah elemen)
print("Isi array:", angka)
print("Panjang array (jumlah elemen):", len(angka))

# 4) Menghitung dan menampilkan jumlah total dari semua elemen dalam array
total = sum(angka)
print("Jumlah total elemen array:", total)

# 5) Menghitung dan menampilkan nilai rata-rata dari elemen array
rata_rata = total / len(angka)
print("Nilai rata-rata elemen array:", rata_rata)