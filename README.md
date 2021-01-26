#  Cryptarithmetic Solver
> Tugas Kecil 1 Mata Kuliah IF2211 Strategi Algoritma 
> Bahasa : Python 3

Program ini akan menyelesaikan permasalahan Cryptarithmetic. Walaupun tidak begitu efektif dan efisien caranya, namun masih berfungsi 😋🤗. Contohnya adalah seperti ini.
```
SEND
MORE+
------
MONEY
```
Keluaran dari contoh diatas adalah seperti dibawah ini.
```
===== CRYPTARITHMETIC SOLVER =====
This program is using a brute force algorithm, so it may take some time depending on your computer power.
You can add more than 1 (one) problem each file. Use `./folder_name/file_name` if it's on another directory.

Enter filename (.txt only): ../test/test1
--- Solving Problem --
Problem: SEND + MORE = MONEY

--- Results ---
1 solution(s) found.
S = 9
E = 5
N = 6
D = 7
M = 1
O = 0
R = 8
Y = 2
Iterations:1451520
Time taken: 148.74766421318054
Press ENTER to exit. To try again, you need to close and reopen the program.
```
**Instalasi**\
Dalam pembuatan executable file, digunakan [PyInstaller](https://www.pyinstaller.org/). Agar menjamin executable dapat dijalankan, mohon jalankan command berikut pada command line.
```
pip install pyinstaller
```

**Cara Penggunaan**
1. Input hanya dapat berupa file, sehingga buatlah terlebih dahulu file bereksistensi `.txt` yang berisi persoalan dengan format seperti contoh. Dalam satu file bisa terdapat lebih dari satu persoalan yang dipisahkan dengan enter. Contohnya seperti ini.

```
FORTY
TEN
TEN+
------
SIXTY

COCA
COLA+
------
OASIS
```
2. Buka command line dan pindah ke folder src.
```
py -3 main.py
```
atau dapat langsung membuka dengan file shortcut executablenya, `Cryptarithmetic Solver` pada folder bin. Sementara file executablenya dapat ditemukan di `./bin/dist/main/main.exe`.

3. Setelah itu, ikuti instruksi pada program dan hasil akan tercetak pada layar. Saat memasukkan alamat file, apabila kesusahan dengan alamat relatifnya ( `./nama_foler/nama_file` )dapat langsung menggunakan alamat directnya seperti ini.
```
D:\IF Tubes Tucil\IF2211 Strategi Algoritma\Tucil 1 Cryptarithmetic\test\test1
```

**Credits** \
Program ini dibuat oleh [@salyamevia](https://github.com/salyamevia) dengan beberapa sumber referensi | Januari 2021