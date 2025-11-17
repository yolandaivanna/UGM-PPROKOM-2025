# konversi_suhu.py
# Modul berisi fungsi-fungsi konversi suhu antar Celcius, Fahrenheit, dan Kelvin

# --- Dari Celcius ---
def celsius_ke_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_ke_kelvin(c):
    return c + 273.15

# --- Dari Fahrenheit ---
def fahrenheit_ke_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_ke_kelvin(f):
    return (f - 32) * 5/9 + 273.15

# --- Dari Kelvin ---
def kelvin_ke_celsius(k):
    return k - 273.15

def kelvin_ke_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32
