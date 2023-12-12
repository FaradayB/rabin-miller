# rabin-miller
{TUGAS 4 KAMSIS}
Kelompok:
1. Faraday Barr Fatahillah (1103213028)
2. Purwantoro Aji Nugroho (1103213002)
3. Amalul Anugrah Amin (1103213054)

Berikut merupakan tugas kami terkait:
Tugas 4 part 1: Rabin-Miller Primality Test
Tugas 4 part 2: Rangkuman dan Program ECC (Eliptical Curve Cryptography)

====================================================================================================
TUGAS 4 PART 1
Pada tugas ini, kami mengimplementasikan sebuah algoritma untuk pencarian angka prima atau bukan
yang dibuat oleh Miller dan Rabin. Pada algoritma ini, terdapat 3 langkah penting:

1. Step 1
pada step ini terdapat pengaplikasian rumus
n - 1 = (2^k) m

step ini akan mendapatkan hasil dari k dan m yang akan digunakan pada Step 3

2. Step 2
pada step ini kami akan mengambil random int number yang di simbolkan sebagai a dimana:
1 < a < n-1 atau 2<= a <= n-2

step ini akan mendapatkan hasil dari a yang akan digunakan pada Step 3

3. Step 3
pada step ini kami akan mengkomputasi perhitungan berikut
pada iterasi pertama (0):
b0 = a^m(mod n)

pada iterasi selanjutnya:
bi = (bi-1)^2 mod n

apa bila pada b0 mendapatkan hasil 1, maka angka yang di test sebuah prima
jika bukan lanjut ke komputasi pada iterasi selanjutnya

apabila di bi, bi sama dengan n - 1 atau bi sama dengan -1, maka angka yang di test sebuah prima
jika bukan akan melakukan terus hingga perulangan selesai dengan cara:
(b*b) mod n
jika perulangan selesai dan kondisi tidak terpenuhi, maka bilangan tersebut bukan prima
Penjelasan detail code ada pada codingan
Keterangan:
n = angka yang di input
k = angka yang didapatkan untuk iterasi pada step 3
m = angka yang dipangkatkan untuk mendapatkan b0
b0 = angka b yang didapatkan saat iterasi ke 0
bi = angka b yang didapatkan saat iterasi setelah ke 0
bi-1 = angka b yang didapatkan pada iterasi sebelumnya





========================================================================================================
TUGAS 4 PART 2

Terdapat rangkuman pada folder
