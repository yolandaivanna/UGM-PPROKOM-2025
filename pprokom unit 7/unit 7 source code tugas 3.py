# Tugas 3 - Program pencatatan nilai mahasiswa (versi diperbaiki)
nilai_mahasiswa = {}  # dict kosong: key = nama, value = nilai (int)

# menambahkan beberapa data awal
nilai_mahasiswa["Andi"] = 85
nilai_mahasiswa["Budi"] = 78
nilai_mahasiswa["Citra"] = 92

# Tampilkan semua nilai
print("Daftar nilai mahasiswa:")
for nama, nilai in nilai_mahasiswa.items():
    print(f"- {nama}: {nilai}")

# Minta input user untuk menambahkan mahasiswa baru
nama_baru = input("\nMasukkan nama mahasiswa baru: ").strip()
while True:
    nilai_input = input("Masukkan nilai (0-100): ").strip()
    try:
        nilai_baru = int(nilai_input)
        if 0 <= nilai_baru <= 100:
            break
        else:
            print("Nilai harus antara 0 sampai 100.")
    except ValueError:
        print("Input tidak valid. Masukkan angka untuk nilai.")

nilai_mahasiswa[nama_baru] = nilai_baru
print(f"\nMahasiswa '{nama_baru}' berhasil ditambahkan dengan nilai {nilai_baru}.")

# Tampilkan kembali daftar nilai terbaru
print("\nDaftar nilai terbaru:")
for nama, nilai in nilai_mahasiswa.items():
    print(f"- {nama}: {nilai}")

