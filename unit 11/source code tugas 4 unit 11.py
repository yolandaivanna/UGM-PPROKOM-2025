# Program Kalkulator Matematika Sederhana
# Nama : [Yolanda Ivana Fidhellia Siswoyo]
# NIM  : [25/556485/SV/25940]

import math

# Fungsi-fungsi operasi matematika
def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan!"
    return a / b

def perpangkatan(a, b):
    return a ** b

def akar_kuadrat(a):
    if a < 0:
        return "Error: Tidak dapat menghitung akar kuadrat dari bilangan negatif!"
    return math.sqrt(a)

# Fungsi utama program
def main():
    while True:
        print("\n- KALKULATOR MATEMATIKA SEDERHANA -")
        print("1. Penjumlahan (A + B)")
        print("2. Pengurangan (A - B)")
        print("3. Perkalian (A * B)")
        print("4. Pembagian (A / B)")
        print("5. Perpangkatan (A ^ B)")
        print("6. Akar Kuadrat (√A)")
        print("7. Keluar")
        print("---------------------------------------------")
        
        pilihan = input("Pilih menu (1-7): ")
        
        if pilihan == '7':
            print("Terima kasih telah menggunakan kalkulator ini!")
            break
        
        # Operasi yang membutuhkan dua bilangan
        if pilihan in ['1', '2', '3', '4', '5']:
            a = float(input("Masukkan bilangan pertama (A): "))
            b = float(input("Masukkan bilangan kedua (B): "))
            
            if pilihan == '1':
                hasil = penjumlahan(a, b)
                print(f"Hasil {a} + {b} = {hasil}")
            elif pilihan == '2':
                hasil = pengurangan(a, b)
                print(f"Hasil {a} - {b} = {hasil}")
            elif pilihan == '3':
                hasil = perkalian(a, b)
                print(f"Hasil {a} * {b} = {hasil}")
            elif pilihan == '4':
                hasil = pembagian(a, b)
                print(f"Hasil {a} / {b} = {hasil}")
            elif pilihan == '5':
                hasil = perpangkatan(a, b)
                print(f"Hasil {a} ^ {b} = {hasil}")
        
        # Operasi akar kuadrat hanya butuh satu bilangan
        elif pilihan == '6':
            a = float(input("Masukkan bilangan (A): "))
            hasil = akar_kuadrat(a)
            print(f"Hasil √{a} = {hasil}")
        
        else:
            print("Pilihan tidak valid! Silakan pilih menu 1–7.")

# Menjalankan program
if __name__ == "__main__":
    main()
