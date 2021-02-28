# Penyusunan Rencana Kuliah dengan *Topological Sort* (Penerapan Decrease and Conquer)
### Sebagai pemenuhan Tugas Kecil 2 IF 2211 Strategi Algoritma Semester II Tahun 2020/2021
---

## Algoritma Decrease and Conquer
**1. Decrease**
Mereduksi persoalan menjadi beberapa persoalan yang lebih kecil. 
Implementasi : 
- Menghapus mata kuliah yang tidak memiliki prasyarat
- Menghapus mata kuliah tersebut dari list prasyarat mata kuliah lain

**2. Conquer**
Memproses satu-upa persoalan secara rekursif. 
Implementasi :
- Memilih mata kuliah yang akan direduksi (tidak memiliki prasyarat)

Data mata kuliah dan prasyarat di simpan dalam bentuk *dictionary*
- Key : mata kuliah yang unik
- Value : mata kuliah prasyarat dari *key*

## Instalasi dan cara menggunakan program
1. Install python3 sesuai dengan petunjuk pada [link berikut](https://www.python.org/downloads/)
2. Pada command prompt, user harus masuk ke dalam direktori src yang berisi kode program.
3. Setelah itu, jalankan command `python3 13519100.py`
4. Selamat menjalankan program!

### Author
Nama : Aulia Adila
NIM  : 13519100
Kelas: K02