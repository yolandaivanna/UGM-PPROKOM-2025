# main.py
# Program utama aplikasi penjualan

from produk import tampilkan_produk, produk_list
from transaksi import hitung_total, hitung_diskon

while True:
    print("\033[1;32m== APLIKASI PENJUALAN TOKO PYTHON ==\033[0m\n")

    tampilkan_produk()

    try:
        pilihan = int(input("\nPilih produk (nomor): "))
        if pilihan not in produk_list:
            print("Produk tidak ditemukan. Coba lagi.\n")
            continue

        jumlah = int(input("Masukkan jumlah beli: "))

        nama_produk, harga = produk_list[pilihan]
        total = hitung_total(harga, jumlah)
        diskon = hitung_diskon(total)
        total_bayar = total - diskon

        print("\n\033[1;32m=== STRUK PEMBAYARAN ===\033[0m")
        print(f"\033[1;35mProduk        : {nama_produk}")
        print(f"Harga Satuan  : Rp{harga}")
        print(f"Jumlah Beli   : {jumlah}")
        print(f"Total Harga   : Rp{total}")
        print(f"Diskon        : Rp{diskon}")
        print(f"Total Bayar   : Rp{total_bayar}\033[0m")

        ulang = input("\nApakah ingin belanja lagi? (y/n): ").lower()
        if ulang != 'y':
            print("\033[1;32mTerima kasih telah berbelanja!\033[0m")
            break

    except ValueError:
        print("Input tidak valid! Silakan coba lagi.\n")
