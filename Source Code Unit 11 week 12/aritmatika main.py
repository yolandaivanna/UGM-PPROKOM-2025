# main.py
# Program utama untuk menggunakan modul aritmatika

import aritmatika

print("=== PROGRAM OPERASI MATEMATIKA ===")
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

print("\nHasil Operasi Menggunakan Modul aritmatika:")
print(f"Penjumlahan: {aritmatika.penjumlahan(a, b)}")
print(f"Pengurangan: {aritmatika.pengurangan(a, b)}")
print(f"Perkalian: {aritmatika.perkalian(a, b)}")
print(f"Pembagian: {aritmatika.pembagian(a, b)}")
print(f"Modulo: {aritmatika.modulo(a, b)}")
print(f"Pangkat: {aritmatika.pangkat(a, b)}")
