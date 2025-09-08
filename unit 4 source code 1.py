umur = int(input("Masukkan umur anda = "))
nilai = int(input("Masukkan nilai tes anda ="))
lulus = "Selamat anda berhak mendapatkakn SIM anda"
gagal = "Maaf anda tidak berhak mendapatkan SIM anda\nsilahkan coba lagi bulan atau tahun depan"
if (umur > 17):
    if (nilai < 60):
        print()
        print(gagal)
    else:
        print()
        print(lulus)
else:
    print()
    print(gagal)
