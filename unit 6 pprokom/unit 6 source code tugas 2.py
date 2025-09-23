# Himpunan awal
nilai = set({3, 6, 9, 2, 5, 7})
print("Himpunan awal:", nilai)

# Menambahkan elemen 1, 4, 8, 10
nilai.update([1, 4, 8, 10])
print("Setelah penambahan:", nilai)

# Menghapus elemen 1, 3, 4, 5, 7, 8, 10
nilai.difference_update([1, 3, 4, 5, 7, 8, 10])
print("Setelah penghapusan:", nilai)
