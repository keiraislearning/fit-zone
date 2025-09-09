tautan situs web deployment: https://keira-nuzahra-fitzone.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab= Pertama, saya membuat folder untuk direktori sesuai dengan nama aplikasi (fitzone) kemudian dalam folder tersebut saya membuat dan mengaktifkan virtual environment lalu menambahkan dependencies didalam file requirements dan di instalisasi. Kedua, membuat projek bernama fit_zone di direktori utama kemudian mengkonfigurasi environment variables proyek, lalu jangan lupa untuk migrasi database. Ketiga, membuat aplikasi main kemudian di daftarkan di setting.py bagian INSTALLED_APPS. Keempat, buka file models.py di bagian main, dan mulai di isi sesuai dengan checklist. Kelima, isi file views.py di dalam main dengan fungsi show_main (berfungsi sebagai menampilkan nama aplikasi serta nama dan kelas) kemudian mengatur routingnya didalam main, setelah itu menambahkan pengaturan url lewat urls.py agar proyek bisa menyambung dan melakukan pemetaan ke rute URL pada aplikasi main. Keenam, buat proyek baru di PWS kemudian edit bagian raw environment sesuai dengan isi .env.prod kemudian menambahkan url deployment PWS pada ALLOWED_HOSTS. Ketujuh, lakukan project command pada halaman PWS.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawab= 
![Bagan Django](Bagan%20Django.jpg)
Kaitannya, urls.py bagian menentukan URL mana yang manggil fungsi apa di views.py. Sedangkan, views.py itu seperti yang berpikir (mengatur logika lalu menentukan template yang ditampilkan). Kemudian models.py dipanggil views.py untuk ambil atau simpan data ke database. Terakhir, HTML bagian yg dilihat user (hasil dari pemilihan views.py)

3. Jelaskan peran settings.py dalam proyek Django!
Jawab= file konfigurasi utama di Django seperti bagian otak dalam tubuh manusia. Semua pengaturan proyek ada disini, seperti database, INSTALLED_APPS, templates, konfigurasi keamanan, dll. settings.py semacam otak pengaturan proyek agar bisa berjalan dgn benar.

4. Bagaimana cara kerja migrasi database di Django?
Jawab= pertama makemigrations (python manage.py makemigrations) membuat file migrasi berdasarkan perubahan model, kemudian migrate (python manage.py migrate) menerapkan migrasi itu ke database.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawab= menurut saya karena Django fitur bawaan yang lumayan banyak kemudian phyton based juga sehingga beginner-friendly. Ada juga strukturnya dengan pola MTV sehingga membiasakan untuk menulis kode scr rapi.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Jawab= Asisten dosen sudah bagus dan sangat membantu dalam tutorialnya kemarin. Ketika ditanyakan juga ia menjelaskannya mudah dipahami dan ramah jadi tidak malu untuk tanya lagi.