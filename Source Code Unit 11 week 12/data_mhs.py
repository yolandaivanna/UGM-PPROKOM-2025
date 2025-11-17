# data_mhs.py

# List untuk menyimpan data mahasiswa
daftar_mhs = []

def tambah_data(nama, nim):
    """Menambahkan data mahasiswa ke list daftar_mhs."""
    data = {"nama": nama, "nim": nim}
    daftar_mhs.append(data)
    return f"Data mahasiswa {nama} ({nim}) berhasil ditambahkan!"

def tampilkan_data():
    """Menampilkan seluruh data mahasiswa."""
    if not daftar_mhs:
        return "Belum ada data mahasiswa."
    
    hasil = "=== DAFTAR MAHASISWA ===\n"
    for i, mhs in enumerate(daftar_mhs, start=1):
        hasil += f"{i}. {mhs['nama']} ({mhs['nim']})\n"
    return hasil
