(1)berapa ukutan type data primitif didalam pemrograman python
jawaban :

<!-- Tipe        Data            Contoh Keterangan
int         10              Bilangan bulat
float       3.14            Bilangan desimal
complex     2+3j            Bilangan kompleks
bool        True            Nilai benar/salah
str         "Hello"         Teks/karakter -->

int = 28 byte
float = 24 byte
bool = 28 byte
complex = 32 byte
str = 42–50 byte atau lebih

<!-- ========================================================================================================================= -->

(2) Perbedaan Array dengan list/linked
Jawaban :

Array adalah struktur data yang menyimpan banyak elemen dalam satu tempat dengan posisi yang berurutan di memori. Setiap elemen memiliki indeks, misalnya indeks 0, 1, 2, dan seterusnya. Pada banyak bahasa pemrograman, ukuran array biasanya ditentukan sejak awal dan elemen di dalamnya biasanya memiliki tipe data yang sama.
Contoh konsep array:

Index : 0 1 2 3
Data : 10 20 30 40

Karena posisinya berurutan, mengambil data berdasarkan indeks biasanya sangat cepat. Misalnya ingin mengambil data indeks ke-2, program bisa langsung menuju posisi tersebut.

List adalah kumpulan data yang lebih fleksibel. Khusus di Python, list sebenarnya bekerja lebih mirip dynamic array, bukan linked list. Ukurannya dapat bertambah atau berkurang secara otomatis.

Contoh:

angka = [10, 20, 30, 40]

angka.append(50)
print(angka)

Hasil:

[10, 20, 30, 40, 50]

Python list juga dapat menyimpan tipe data yang berbeda:

data = [10, "Alex", 3.5, True]

Sedangkan Linked List adalah struktur data yang setiap elemennya disebut node. Setiap node menyimpan data dan sebuah penghubung atau link menuju node berikutnya
