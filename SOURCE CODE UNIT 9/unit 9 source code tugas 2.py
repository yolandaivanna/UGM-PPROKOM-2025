# Program: Mengganti Nama Teman dalam List

# 1) Meminta user memasukkan 5 nama dan menyimpannya dalam list
nama_teman = []
for i in range(5):
    nama = input(f"Masukkan nama teman ke-{i+1}: ")
    nama_teman.append(nama)

# 2) Menampilkan semua nama dalam list dengan urutan indeksnya
print("\nDaftar nama teman:")
for i, nama in enumerate(nama_teman):
    print(f"Indeks {i}: {nama}")

# 3) Menanyakan user ingin mengganti nama teman pada indeks ke berapa
indeks = int(input("\nIngin mengganti nama pada indeks ke berapa? "))

# 4) Meminta input nama penggantinya, lalu melakukan pergantian pada list
if 0 <= indeks < len(nama_teman):
    nama_baru = input("Masukkan nama pengganti: ")
    nama_teman[indeks] = nama_baru
else:
    print("Indeks tidak valid!")

# 5) Menampilkan list nama yang sudah diperbarui
print("\nDaftar nama teman yang sudah diperbarui:")
for i, nama in enumerate(nama_teman):
    print(f"Indeks {i}: {nama}")