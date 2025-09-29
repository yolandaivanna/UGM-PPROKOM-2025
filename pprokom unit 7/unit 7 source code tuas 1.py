# Tugas 1 - dictionary buah_buahan
buah_buahan = {
    "Apel": 15000,
    "Jeruk": 10000,
    "Anggur": 25000
}

# 1) Tampilkan harga jeruk.
print("1) Harga Jeruk: Rp{:,}".format(buah_buahan["Jeruk"]).replace(",", "."))

# 2) Tambahkan buah mangga dengan harga Rp12.000 kemudian tampilkan dictionary terbaru.
buah_buahan["Mangga"] = 12000
print("\n2) Setelah menambahkan Mangga:")
for nama, harga in buah_buahan.items():
    print(f"- {nama}: Rp{harga:,}".replace(",", "."))

# 3) Perbarui harga anggur menjadi Rp20.000 kemudian tampilkan dictionary terbaru.
buah_buahan["Anggur"] = 20000
print("\n3) Setelah memperbarui harga Anggur:")
for nama, harga in buah_buahan.items():
    print(f"- {nama}: Rp{harga:,}".replace(",", "."))

# 4) Hapus buah jeruk kemudian tampilkan dictionary terbaru.
del buah_buahan["Jeruk"]
print("\n4) Setelah menghapus Jeruk:")
for nama, harga in buah_buahan.items():
    print(f"- {nama}: Rp{harga:,}".replace(",", "."))
