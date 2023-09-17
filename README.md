Nama    : Alifa Hanania Ardha

NPM     : 2206024392

Kelas   : PBP B

# [Item Tracker App](https://item-tracker.adaptable.app/main/)
## TUGAS 3
1. Pengiriman data dengan POST tidak dapat terlihat langsung di URL karena tidak terlihat pada tubuh HTTP, sedangkan dengan GET kita dapat melihat datanya pada URL. Kemudian, GET membatasi ukuran data yang dapat dikirim, sedangkan POST tidak sehingga POST lebih sering digunakan ketika ingin mengirim data berukuran kompleks. Jadi, untuk data yang akan mengubah sistem seperti mengubah sesuatu di database, sabaiknya menggunakan POST karena lebih aman.
   
2. Utamanya, XML dan JSON digunakan untuk penyimpanan dan pengiriman data, sedangkan HTML untuk bagaimana kita akan menampilkan data tersebut. Lalu, perbedaan dari XML dan JSON adalah XML menggunakan tag untuk merepresentasikan datanya, sedangkan JSON menggunakan key dan value.

3. 
## TUGAS 2
1. - Membuat direktori lokal bernama item tracker
   - Membuat repository di github bernama item_tracker
   - Menyambungkan repository github dengan direktori lokal dan membuat branching
   - Membuat aplikasi django bernama main
   - Membuat template html bernama main yang berisi nama dan kelas yang akan ditampilkan pada aplikasi
   - Menambahkan function pada models.py dan menambahkan atribut name, amount, dan description
   - Mendefinisikan function dengan parameter request pada views.py
   - Mengatur dan mengonfigurasi routing url pada aplikasi main melalui urls.py
   - Melakukan testing melalui tests.py
  
     
2. <img width="445" alt="image" src="https://github.com/hunnania/item_tracker/assets/119483290/493c40e4-3c8d-4bec-aac3-571e2d6e58b8">
3. Virtual environment adalah alat yang membantu mengisolasi dependensi yang dibutuhkan proyek-proyek berbeda secara terpisah yang dibatasi dengan membuat lingkungan terisolasi. Virtual environment digunakan agar proyek kita tidak tumpang-tindih dengan proyek lainnya, menjaga proyek terorganisir, memudahkan pengelolaan versi paket-paket yang digunakan, meningkatkan keamanan proyek, dan memudahkan untuk membagikan proyek kita kepada orang lain. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi tidak dianjurkan.
4. - MVC (Model-View-Controller) adalah pola desain arsitektur yang umum digunakan dalam berbagai aplikasi. Komponen MVC terdiri dari:
     * Model: Komponen yang berisi logika bisnis dan mengelola data. Model memungkinkan untuk akses ke data, berkomunikasi dengan controller, dan mengelola informasi yang akan ditampilkan.
     * View: Komponen yang berhubungan dengan antarmuka pengguna dari data yang dihasilkan Model yang terdiri dari HTML atau CSS.XML. View juga berhubungan dengan controller untuk menampilkan aplikasi yang dinamis.
     * Controller: Komponen yang mengatur interaksi pengguna seperti menerima, memproses input, dan menentukan apa yang terjadi selanjutnya serta mengelola alur aplikasi.
   - MVT (Model-View-Template) adalah turunan dari MVC yang memiliki fokus pada pengembangan web menggunakan Python. MVT terdiri dari:
     * Model: Komponen yang menyimpan data dan logika aplikasi.
     * View: Komponen yang menampilkan data dari model dan menghubungkannya dengan template.
     * Template: Komponen yang mengatur tampilan antarmuka pengguna
   - MVVM (Model-View-ViewModel) adalah pola desain yang umumnya digunakan untuk aplikasi berbasis data-binding. MVVM terdiri dari:
     * Model: Komponen yang mengelola logika bisnis dan data.
     * View: Komponen yang berfokus mengatur tampilan data kepada pengguna.
     * ViewModel: Komponen yang menjadi perantara antara Model dan View dan berisi logika yang mengatur data agar sesuai dengan yang akan ditampilkan di view.
       
  
   Secara ringkas, perbedaan utamanya adalah ketiga pola desain ini memiliki komponen perantara yang berbeda-beda (controller, template, atau viewmodel) dan memiliki fokus utama yang berbeda-beda dalam pengembangan perangkat lunak.
