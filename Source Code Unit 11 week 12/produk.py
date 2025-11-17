# produk.py
# Modul berisi daftar produk dan harga

produk_list = {
    1: ("Keyboard", 150000),
    2: ("Mouse", 80000),
    3: ("Flashdisk", 50000)
}

def tampilkan_produk():
    print("\033[1;32m=== DAFTAR PRODUK ===\033[0m")
    for nomor, (nama, harga) in produk_list.items():
        print(f"{nomor}. {nama} - Rp{harga}")
