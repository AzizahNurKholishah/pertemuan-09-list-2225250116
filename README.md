
# Pertemuan 09 – List/Array dan Pengolahan Data Numerik Sederhana

| Keterangan | informasi |
|---|---|
| Nama | Azizah Nur Kholishah |
| NIM | 2225250116 |
| Kelas | 3E|

## Tujuan 

Mengolah kumpulan data numerik menggunakan list Python, memahami penggunaan indeks dan slicing, memanipulasi elemen list, menghitung statistik sederhana, melakukan penyaringan data berdasarkan kondisi, serta membuat fungsi untuk pengolahan data numerik.

## Struktur Folder

```text
pertemuan-09-list-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_buat_list.py
│   ├── 02_indeks_slicing.py
│   ├── 03_manipulasi_list.py
│   ├── 04_agregasi_nilai.py
│   ├── 05_filter_kelulusan.py
│   └── 06_fungsi_statistik.py
└── praktik/
    └── analisis_nilai_mahasiswa.py
```

## Cara Menjalankan

```bash
   python praktik/analisis_nilai_mahasiswa.py
   python praktik/analisis_nilai_mahasiswa.py
```

## Test Case

| Data yang Diuji | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| `[60, 70, 80]` – Rata-rata | 70.00 | 70.00 | Berhasil |
| `[60, 70, 80]` – Minimum/Maksimum | 60 / 80 | 60 / 80 | Berhasil |
| `[60, 70, 80]` – Jumlah lulus | 3 | 3 | Berhasil |
| `[59, 60, 61]` – Batas kelulusan | 2 mahasiswa lulus | 2 mahasiswa lulus | Berhasil |
| `[]` – Rata-rata list kosong | Tidak error | 0 | Berhasil | 

## Refleksi

 saya memahami bahwa list dapat digunakan untuk menyimpan banyak data dalam satu variabel dan mengolahnya menggunakan fungsi seperti `len()`, `sum()`, `min()`, dan `max()`. Kesalahan yang berhasil saya perbaiki adalah penanganan list kosong pada fungsi rata-rata agar program tidak mengalami error saat tidak ada data yang dihitung.

## Exit Ticket

1. **Keuntungan menggunakan list:** List dapat menyimpan banyak elemen dalam satu variabel sehingga data lebih mudah diolah.
2. **Kesalahan indeks yang mungkin terjadi:** Mengakses indeks di luar rentang list dapat menyebabkan `IndexError`.
3. **Materi sebelumnya yang membantu:** Perulangan, seleksi, dan fungsi membantu mengolah setiap elemen list serta memeriksa kondisi kelulusan.
4. **Persiapan untuk materi string:** Memahami indeks, slicing, dan perulangan untuk mengakses serta mengolah karakter dalam string.

