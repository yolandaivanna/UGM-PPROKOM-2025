# main.py
# Program utama untuk konversi suhu menggunakan modul konversi_suhu

import konversi_suhu

print("=== PROGRAM KONVERSI SUHU ===")
print("Pilih satuan asal:")
print("1. Celcius")
print("2. Fahrenheit")
print("3. Kelvin")

pilihan = input("Masukkan pilihan (1/2/3): ")

# Input nilai suhu dari pengguna
suhu = float(input("Masukkan nilai suhu: "))

print("\n=== HASIL KONVERSI ===")

if pilihan == "1":
    print(f"{suhu}°C = {konversi_suhu.celsius_ke_fahrenheit(suhu)}°F")
    print(f"{suhu}°C = {konversi_suhu.celsius_ke_kelvin(suhu)} K")

elif pilihan == "2":
    print(f"{suhu}°F = {konversi_suhu.fahrenheit_ke_celsius(suhu)}°C")
    print(f"{suhu}°F = {konversi_suhu.fahrenheit_ke_kelvin(suhu)} K")

elif pilihan == "3":
    print(f"{suhu} K = {konversi_suhu.kelvin_ke_celsius(suhu)}°C")
    print(f"{suhu} K = {konversi_suhu.kelvin_ke_fahrenheit(suhu)}°F")

else:
    print("Pilihan tidak valid. Silakan jalankan ulang program.")
