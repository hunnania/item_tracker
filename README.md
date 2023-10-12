Nama    : Alifa Hanania Ardha

NPM     : 2206024392

Kelas   : PBP B

# [Item Tracker App](https://item-tracker.adaptable.app/main/)
## TUGAS 6
1. Synchronous programming akan menunggu suatu perintah selesai dikerjakan dahulu dan baru akan mengerjakan perintah selanjutnya secara berurutan, sedangkan asynchronous dapat melakukan perintah yang berbeda di waktu yang bersamaan/tidak harus menunggu perintah sebelumnya selesai.
2. Maksud dari event-driven programming adalah sebuah program tidak akan langsung dijalankan dari awal hingga akhir, tetapi ia akan menunggu peristiwa/event dari pengguna, misalnya pengguna menekan tombol. Contohnya pada tugas ini adalah pada tombol "Add Item by AJAX" ditekan oleh pengguna, tombol akan memanggil fungsi addProduct() dan menjalankan kode yang ada di dalam blok fungsi yang dipanggil.
3. Penerapan asynchronous pada AJAX:
   - Permintaan data dari server (request) secara asynchronous agar server tetap responsif sembari menunggu data
   - Fungsi Callback yang menangani data yang diterima dari server dan menjalankan kode yang sesuai dengan data
   - Event Handling, AJAX menggunakan peristiwa (events) untuk menangani hasil permintaan
   - XMLHttpRequest Object atau metode seperti `fetch` untuk membuat permintaan ke server
   - Async/Await. `async` dapat mengembalikan nilai secara asinkronus dan `await` menunggu hasil dari fungsi `async`
4. Fetch API:
   - Fetch API adalah bagian dari spesifikasi JavaScript modern dan disertakan dalam semua browser modern
   - Promised-Based, kode lebih bersih dan mudah dipahami dalam menangani permintaan asynchronous.
   - Fetch API lebih ringan karena tidak memerlukan pustaka eksternal seperti jQuery
   jQuery:
   - jQuery merupakan pustaka JavaScript yang besar dan mencakup berbagai fungsi dan manajemen peristiwa selain AJAX sehingga memudahkan UI
   - jQuery lebih kompatibel untuk lintas browser, termasuk browser lama
  
   Menurut saya, jika kita membuat aplikasi modern yang ditujukan untuk browser modern lebih baik menggunakan Fetch API, sedangkan jika kita membuat aplikasi yang memerlukan UI yang kompleks dan banyak atau perlu didukung browser lama lebih baik menggunakan jQuery.
5. - Menambahkan fungsi `get_product_json` dan `add_product_ajax` pada views.py
   - Melakukan routing pada fungsi baru tersebut di urls.py
   - Menambahkan fungsi-fungsi JavaScript pada main.html seperti `getProducts()` untuk mengambil semua data server, `refreshProduct()` untuk menampilkan data menggunakan AJAX, dan `addProduct()` untuk menambahkan data dengan AJAX
   - Membuat form modal yang digunakan untuk menambahkan item menggunakan AJAX
   - Menambahkan tombol `Add Item by AJAX` pada navbar
     
## TUGAS 5
1. - Element selector: Memilih semua elemen yang sejenis. Tepat untuk digunakan jika kita ingin mengaplikasikan style yang sama pada elemen tersebut di semua dokumen.
   - Class selector: Memilih semua elemen yang berada di dalam class tersebut. Tepat untuk digunakan saat ingin mengubah semua elemen pada class tertentu.
   - ID Selector: Memilih elemen yang memiliki ID tertentu. Karena ID bersifat unik pada satu halaman, tepat untuk digunakan jika kita hanya inginmengubah sebuah elemen secara spesifik.
  
2. - header, biasanya untuk bagian awal sebuah halaman/dokumen.
   - div, biasanya digunakan sebagai wadah/kontainer untuk mengelompokkan elemen-elemen.
   - p, digunakan untuk menandai teks yang bersifat paragraf.
   - title, digunakan untuk memberi judul halaman.
   - label, untuk menghubungkan teks/label dengan sebuah formulir/input area.

3. Margin biasanya digunakan saat ingin mengatur jarak antar elemen sekitarnya, margin tidak dapat diisi oleh warna atau gambar, margin tidak memengaruhi tata letak elemen. Padding digunakan untuk mengatur jarak antara konten elemen dengan batas elemen itu sendiri, padding dapat diisi warna atau gambar, padding memengaruhi tata letak elemen.

4. Tailwind umumnya digunakan untuk mengbuat/customize user interface, sedangkan bootstrap umumnya untuk membuat aplikasi responsif. Lalu, bootstrap memiliki banyak komponen desain yang sudah tersedia. Kemudian, bootstrap memiliki tampilan bawaan sehingga lebih konsisten, sedangkan tailwind tidak ada.

Kita sebaiknya menggunakan Tailwind dibandingkan Bootstrap ketika proyek kita memerlukan banyak kostumisasi yang unik dan lebih terfokus pada front-end. Sebaliknya, kita sebaiknya menggunakan bootstrap dibandingkan tailwind jika proyek kita lebih banyak kerja pada back-end.

5. - Saya memutuskan untuk menggunakan CSS dan mencari tutorial-tutorialnya di internet.
   - Mencari desain login page yang saya sukai.
   - Mulai mendesain login page menggunakan CSS dan diletakkan pada file html yang sama.
   - Memilih palet warna, mengatur font, dan mengatur tata letak elemen
   - Mendesain register page, lebih kurang mengikuti desain yang sudah dilakukan pada page login
   - Mendesain main page dengan menambahkan navigation bar yang berisi nama aplikasi, tombol add item, dan tombol logout
   - Mendesain card agar tampilan daftar item lebih menarik

## TUGAS 4
1. DJango UserCreationForm digunakan untuk membuat user untuk sebuah aplikasi web. UserCreationForm memiliki 3 atribut yaitu username, password1, dan password2 (digunakan untuk mengkonfirmasi password1).

Kelebihan dari UserCreationForm:
* Mudah digunakan karena ia merupakan formulir bawaan yang sudah bisa langsung dipakai
* Ia bisa memvalidasi data yang di-input pengguna secara otomatis
* Mudah untuk menyimpan data pengguna ke database

Kekurangan:
* Formulir yang tersedia cukup standar sehingga jika kita ingin atribut yang lebih kompleks, kita perlu merancangnya secara khusus sendiri
* Tampilan standar sehingga jika kita ingin meningkatkan keestetikaannya, kita perlu membuat template tambahan
* Ia bergantung pada model User bawaan Django sehingga ketika kita ingin menggunakan "User" kita sendiri, kita juga perlu menyesuaikannya pada UserCreationForm
  
2. Autentikasi adalah proses saat memverifikasi identitas user seperti username dan password. Setelah autentikasi selesai, dilanjutkan dengan proses otorisasi yaitu menentukan hal apa saja yang bisa dilakukan user pada web berdasarkan role user tersebut. Kedua proses tersebut sangat penting untuk keamanan, memastikan bahwa user yang bisa mengakses web adalah user yang telah terautentikasi. Kemudian, otorisasi memberikan kita kontrol terhadap hak akses aplikasi. Setelah itu, autentikasi juga memastikan user hanya bisa mengakses data-datanya sendiri, ini penting untuk privasi.

3. Cookies adalah data berukuran kecil yang disimpan pada browser user pada periode waktu tertentu. Biasanya berisi informasi tentang aktivitas pengguna pada aplikasi web.
  
Django menggunakan cookies untuk menyimpan data sesi pengguna. Cookies sesi digunakan untuk menyimpan data sesi yang dapat diakses oleh server web setiap kali permintaan dari klien dikirim.

4. Data cookies tidak berbahaya untuk aplikasi web itu sendiri. Akan tetapi, jika data-data pada cookies tersebut jatuh ke tangan yang salah, mereka dapat mengakses, mencuri, atau menyadap informasi-informasi pengguna yang bersifat privasi.
   
5. - Membuat function register, login_user, dan logout_user pada views.py
   - Membuat tampilan halaman login dan register dengan html
   - Menambahkan url-url untuk function yang sudah ditambahkan tadi pada urls.py
   - Pada views.py, menambahkan @login_required sehingga setiap user perlu login terlebih dahulu
   - Menghubungkan user dengan model dengan mengubah menjadi `products = Product.objects.filter(user=request.user)` dan `product.user = request.user` pada function input item
   - Menambahkan `response.set_cookie('last_login', str(datetime.datetime.now()))` pada function login dan `last_login': request.COOKIES['last_login'],` pada show_main untuk menyimpan data login user pada cookies
     
## TUGAS 3
1. Pengiriman data dengan POST tidak dapat terlihat langsung di URL karena tidak terlihat pada tubuh HTTP, sedangkan dengan GET kita dapat melihat datanya pada URL. Kemudian, GET membatasi ukuran data yang dapat dikirim, sedangkan POST tidak sehingga POST lebih sering digunakan ketika ingin mengirim data berukuran kompleks. Jadi, untuk data yang akan mengubah sistem seperti mengubah sesuatu di database, sabaiknya menggunakan POST karena lebih aman.
   
2. Utamanya, XML dan JSON digunakan untuk penyimpanan dan pengiriman data, sedangkan HTML untuk bagaimana kita akan menampilkan data tersebut. Lalu, perbedaan dari XML dan JSON adalah XML menggunakan tag untuk merepresentasikan datanya, sedangkan JSON menggunakan key dan value.

3. Pertama, JSON memiliki sintaks yang mudah dibaca oleh manusia. Kedua, kebanyakan bahasa pemrograman mendukung dalam pembuatan JSON. Ketiga, JSON memiliki ukuran yang lebih ringan. Keempat, format JSON sesuai dengan prinsip pembuatan dan pengembangan layanan web umumnya.

4. - Membuat base.html sebagai template untuk halam web lainnya
   - Membuat struktur form pada forms.py dan menambahkan field yang dibutuhkan untuk aplikasi saya.
   - Membuat fungsi input_item yang akan menerima data saat user men-submit data dari form.
   - Menambahkan path URL input-item pada urls.py
   - Membuat tampilah laman input-item dengan input_item.html
   - Membuat tabel yang dapat menampilkan data di aplikasi melalui main.html
   - Membuat fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id pada views.py
   - Menambahkan 4 path URL di urls.py untuk keempat fungsi yang baru ditambahkan pada views.py tersebut<br>
  
5. - HTML<br>
     <img width="641" alt="image" src="https://github.com/hunnania/item_tracker/assets/119483290/31dd0e04-39ed-425a-b071-ae6727a454e0">

   - JSON<br>
     <img width="643" alt="image" src="https://github.com/hunnania/item_tracker/assets/119483290/0260dc9e-6b44-4b2b-80f6-3f93118247ee">

   - XML<br>
     <img width="637" alt="image" src="https://github.com/hunnania/item_tracker/assets/119483290/30e5e9e6-17e3-4530-a5f3-5a7e6bfced49">

   - JSON by ID<br>
     <img width="642" alt="image" src="https://github.com/hunnania/item_tracker/assets/119483290/3264bdb6-1071-43ee-9674-678f9191d9ad">

   - XML by ID<br>
     <img width="642" alt="image" src="https://github.com/hunnania/item_tracker/assets/119483290/4655aa63-85eb-4e58-8a02-9d7d81c3db7e">

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
