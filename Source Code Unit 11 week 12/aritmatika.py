# aritmatika.py
# Modul berisi fungsi-fungsi operasi matematika dasar

def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian dengan nol tidak diperbolehkan."

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Modulo dengan nol tidak diperbolehkan."

def pangkat(a, b):
    return a ** b
