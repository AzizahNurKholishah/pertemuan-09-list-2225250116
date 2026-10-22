def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []
    for nilai in data:
        if nilai >= batas:
            lulus.append(nilai)
    return lulus


# PROGRAM UTAMA
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

banyak_data = len(nilai)
total = sum(nilai)
rata = rata_rata(nilai)
minimum = min(nilai)
maksimum = max(nilai)

lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = banyak_data - jumlah_lulus

print("=== RINGKASAN STATISTIK NILAI ===")
print(f"Seluruh nilai        : {nilai}")
print(f"Banyak data          : {banyak_data}")
print(f"Total nilai          : {total}")
print(f"Rata-rata             : {rata:.2f}")
print(f"Nilai minimum         : {minimum}")
print(f"Nilai maksimum        : {maksimum}")
print(f"Nilai mahasiswa lulus : {lulus}")
print(f"Jumlah lulus          : {jumlah_lulus}")
print(f"Jumlah belum lulus    : {jumlah_belum_lulus}")


# TEST CASE
print("\n=== PENGUJIAN FUNGSI ===")

data_uji = [60, 70, 80]
print("Rata-rata [60, 70, 80]:", f"{rata_rata(data_uji):.2f}")
print("Minimum:", min(data_uji))
print("Maksimum:", max(data_uji))
print("Jumlah lulus:", len(nilai_lulus(data_uji)))

data_batas = [59, 60, 61]
print("Jumlah lulus [59, 60, 61]:", len(nilai_lulus(data_batas)))

data_kosong = []
print("Rata-rata list kosong:", rata_rata(data_kosong))