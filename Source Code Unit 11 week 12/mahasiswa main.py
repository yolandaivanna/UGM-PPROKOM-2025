# main.py

import data_mhs

while True:
    print("\n=== MENU DATA MAHASISWA ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Keluar")

    menu = input("Pilih menu (1-3): ")

    if menu == "1":
        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM: ")
        print(data_mhs.tambah_data(nama, nim))

    elif menu == "2":
        print(data_mhs.tampilkan_data())

    elif menu == "3":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")
