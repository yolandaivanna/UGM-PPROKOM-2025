# Soal 3: Operasi Himpunan

set_A = {20, 30, 40, 45, 50, 60}
set_B = {25, 30, 35, 40, 45}
set_C = {30, 40, 50, 70, 80}
set_D = {40, 50, 60, 90, 100}

# a. Irisan set_A, set_C, dan set_D
hasil_a = set_A & set_C & set_D
print("a. Irisan set_A, set_C, set_D =", hasil_a)

# b. Gabungan set_A dan set_B, lalu selisih dengan set_D
hasil_b = (set_A | set_B) - set_D
print("b. (set_A ∪ set_B) - set_D =", hasil_b)

# c. Selisih simetris set_B dan set_C
hasil_c = set_B ^ set_C
print("c. set_B Δ set_C =", hasil_c)

# d. Gabungan set_A dengan set_B, serta set_C dengan set_D, lalu irisan keduanya
hasil_d = (set_A | set_B) & (set_C | set_D)
print("d. (set_A ∪ set_B) ∩ (set_C ∪ set_D) =", hasil_d)