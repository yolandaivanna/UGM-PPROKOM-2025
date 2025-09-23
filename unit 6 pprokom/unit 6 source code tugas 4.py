angka = {10, 20, 30, 40, 50}

# Menggunakan remove()
angka.remove(30)
print("Setelah remove(30):", angka)

# Reset set untuk contoh discard
angka = {10, 20, 30, 40, 50}
angka.discard(30)
print("Setelah discard(30):", angka)

# Menggunakan remove() (akan error karena 99 tidak ada)
try:
    angka.remove(99)
except KeyError:
    print("Error: 99 tidak ada di set (remove)")

# Menggunakan discard() (aman, tidak error)
angka.discard(99)
print("Setelah discard(99):", angka)