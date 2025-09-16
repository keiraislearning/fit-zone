tautan situs web deployment: https://keira-nuzahra-fitzone.pbp.cs.ui.ac.id/

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Jawab = Data delivery itu penting supaya informasi dari server bisa sampai ke user dengan cepat, aman, dan akurat. Mulai dari meningkatkan pengalaman, efisiensi operasi, dan masih banyak lagi. Tanpa data delivery yang bagus maka aplikasi dapat menjadi lambat atau data yang ditampilkan nggak akurat.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Jawab = Menurut saya, lebih baik JSON dikarenakan ringan sehingga lebih cepat diproses dan juga mudah dibaca. Selain itu, struktur datanya juga simpel sehingga lebih mudah untuk diubah menjadi objek diberbagai bahasa pemrogaman.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Jawab = Method tersebut penting karena berfungsi untuk ngecek apakah data yang dikirim user sesuai aturan form. Sehingga data yang masuk database bersih dan sesuai format, hal ini juga mengurangi error karena data tidak sesuai.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Jawab = Fungsi csrf_token dalam pembuatan form adalah untuk mencegah serangan berbahaya. Tanpa token ini, memungkinkan pihak luar untuk melakukan tindakan berbahaya atas nama pengguna selain itu permintaan dapat ditolak oleh server. Dengan token ini, django bisa verifikasi kalau request itu beneran dari website kita sendiri.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab = Pertama, membuat form FitForm di forms.py yang terhubung ke model.py. Kedua, membuat views di views.py untuk menampilkan daftar produk, tambah produk, lihat detail produk, dan menampilkan data XML/JSON. Ketiga, membuat URL routing di urls.py. Keempat, membuat tampilannya di bagian templates, untuk daftar produk, tambah produk, dan tampilan detail produk. Kelima, mengecek semua fitur di localhost untuk melihat apakah ada error.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Jawab = Tutorial di website sudah sangat membantu dan penjelasannya mudah dipahami juga.

7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
Jawab = ![XML](XML.jpg)
![JSON](JSON.jpg)