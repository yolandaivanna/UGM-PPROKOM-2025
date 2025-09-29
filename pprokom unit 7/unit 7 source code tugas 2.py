# Tugas 2 - dictionary stok_buku
stok_buku = {
    "Harry Potter": 10,
    "Laskar Pelangi": 15,
    "Bumi Manusia": 7,
    "Dilan 1990": 20
}

# 1) Tampilkan semua judul buku dan stoknya.
print("Daftar buku dan stok:")
for judul, stok in stok_buku.items():
    print(f"Buku: {judul} – Stok: {stok}")

# 2) Minta input dari user untuk menambah buku baru.
print("\nTambah buku baru:")
judul_baru = input("Masukkan judul buku baru: ").strip()
while True:
    jumlah_input = input("Masukkan jumlah stok awal (angka): ").strip()
    if jumlah_input.isdigit():
        jumlah_stok = int(jumlah_input)
        break
    else:
        print("Input tidak valid. Masukkan angka untuk stok.")

# Tambahkan ke dictionary
stok_buku[judul_baru] = jumlah_stok
print(f"\nBuku '{judul_baru}' berhasil ditambahkan dengan stok {jumlah_stok}.")

# Tampilkan dictionary stok_buku terbaru
print("\nStok buku terbaru:")
for judul, stok in stok_buku.items():
    print(f"- {judul}: {stok}")
