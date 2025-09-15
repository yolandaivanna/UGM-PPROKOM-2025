# Memasukkan data siswa dari user
nama1 = input("Masukkan nama siswa 1: ")
nilai1 = int(input("Masukkan nilai siswa 1: "))

nama2 = input("Masukkan nama siswa 2: ")
nilai2 = int(input("Masukkan nilai siswa 2: "))

nama3 = input("Masukkan nama siswa 3: ")
nilai3 = int(input("Masukkan nilai siswa 3: "))

nama4 = input("Masukkan nama siswa 4: ")
nilai4 = int(input("Masukkan nilai siswa 4: "))

nama5 = input("Masukkan nama siswa 5: ")
nilai5 = int(input("Masukkan nilai siswa 5: "))

# Mengecek kelulusan tanpa loop
if nilai1 >= 70:
    print(nama1, "Lulus")
else:
    print(nama1, "Tidak Lulus")

if nilai2 >= 70:
    print(nama2, "Lulus")
else:
    print(nama2, "Tidak Lulus")

if nilai3 >= 70:
    print(nama3, "Lulus")
else:
    print(nama3, "Tidak Lulus")

if nilai4 >= 70:
    print(nama4, "Lulus")
else:
    print(nama4, "Tidak Lulus")

if nilai5 >= 70:
    print(nama5, "Lulus")
else:
    print(nama5, "Tidak Lulus")
