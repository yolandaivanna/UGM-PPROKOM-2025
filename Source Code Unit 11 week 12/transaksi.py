# transaksi.py
# Modul untuk menghitung total dan diskon

def hitung_total(harga, jumlah):
    return harga * jumlah

def hitung_diskon(total):
    if total >= 400000:
        return total * 0.10
    elif total >= 200000:
        return total * 0.05
    else:
        return 0