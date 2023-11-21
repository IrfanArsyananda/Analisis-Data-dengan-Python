=============
Kumpulan Data Berbagi Sepeda
=============

Hadi Fanaee-T

Laboratorium Kecerdasan Buatan dan Pendukung Keputusan (LIAAD), Universitas Porto
INESC Porto, Kampus da FEUP
Rua Dr
4200 - 465 Porto, Portugal


============
Latar belakang
============

Sistem berbagi sepeda adalah generasi baru persewaan sepeda tradisional di mana seluruh proses mulai dari keanggotaan, persewaan, dan pengembalian
kembali menjadi otomatis. Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari posisi tertentu dan kembali lagi
kembali pada posisi lain. Saat ini, terdapat sekitar lebih dari 500 program berbagi sepeda di seluruh dunia yang terdiri dari
lebih dari 500 ribu sepeda. Saat ini, terdapat minat yang besar terhadap sistem ini karena peran pentingnya dalam lalu lintas,
masalah lingkungan dan kesehatan.

Terlepas dari penerapan sistem berbagi sepeda di dunia nyata yang menarik, karakteristik data yang dihasilkan oleh
sistem ini membuatnya menarik untuk penelitian. Berbeda dengan layanan transportasi lain seperti bus atau kereta bawah tanah, durasinya
posisi perjalanan, keberangkatan dan kedatangan dicatat secara eksplisit dalam sistem ini. Fitur ini mengubah sistem bike sharing menjadi
jaringan sensor virtual yang dapat digunakan untuk merasakan mobilitas di kota. Oleh karena itu, diharapkan menjadi hal yang paling penting
peristiwa di kota dapat dideteksi melalui pemantauan data ini.

============
Himpunan data
============
Proses persewaan sepeda sangat berkorelasi dengan kondisi lingkungan dan musim. Misalnya, kondisi cuaca,
curah hujan, hari dalam seminggu, musim, jam dalam sehari, dll. dapat mempengaruhi perilaku sewa. Kumpulan data inti terkait dengan
catatan sejarah dua tahun yang sesuai dengan tahun 2011 dan 2012 dari sistem Capital Bikeshare, Washington D.C., AS yang merupakan
tersedia untuk umum di http://capitalbikeshare.com/system-data. Kami mengumpulkan data setiap dua jam dan setiap hari, lalu
mengekstraksi dan menambahkan informasi cuaca dan musiman yang sesuai. Informasi cuaca diambil dari http://www.freemeteo.com.

============
Tugas terkait
============

- Regresi:
Prediksi jumlah sewa sepeda setiap jam atau harian berdasarkan lingkungan dan musim.

- Deteksi Peristiwa dan Anomali:
Jumlah sepeda sewaan juga berkorelasi dengan beberapa peristiwa di kota yang mudah dilacak melalui mesin pencari.
Misalnya, kueri seperti "30-10-2012 washington d.c." di Google menampilkan hasil terkait Badai Sandy. Beberapa peristiwa penting tersebut adalah
diidentifikasi dalam [1]. Oleh karena itu data dapat digunakan untuk validasi algoritma deteksi anomali atau peristiwa juga.


============
File
============

- Baca saya.txt
- hour.csv : jumlah berbagi sepeda dikumpulkan setiap jam. Catatan: 17379 jam
- day.csv - jumlah berbagi sepeda dikumpulkan setiap hari. Catatan: 731 hari


============
Karakteristik kumpulan data
============
Hour.csv dan day.csv memiliki kolom berikut, kecuali hr yang tidak tersedia di day.csv

- instan: rekor indeks
- hari ini : tanggal
- musim : musim (1: musim semi, 2: musim panas, 3: musim gugur, 4: musim dingin)
- tahun : tahun (0: 2011, 1:2012)
- bulan: bulan (1 hingga 12)
- jam : jam (0 hingga 23)
- hari libur : hari cuaca libur atau tidak (disarikan dari http://dchr.dc.gov/page/holiday-schedule)
- hari kerja : hari dalam seminggu
- hari kerja : jika hari bukan akhir pekan atau hari libur adalah 1, sebaliknya adalah 0.
+ cuaca :
- 1: Cerah, Sedikit awan, Berawan sebagian, Berawan sebagian
- 2: Kabut + Berawan, Kabut + Awan pecah, Kabut + Sedikit awan, Kabut
- 3: Salju Ringan, Hujan Ringan + Badai Petir + Awan Tersebar, Hujan Ringan + Awan Tersebar
- 4: Hujan Lebat + Palet Es + Badai Petir + Kabut, Salju + Kabut
- temp : Suhu normal dalam Celsius. Nilainya dibagi menjadi 41 (maks)
- atemp : Menormalkan suhu perasaan dalam Celsius. Nilainya dibagi 50 (maks)
- hum: Kelembapan yang dinormalisasi. Nilainya dibagi menjadi 100 (maks)
- Kecepatan Angin: Kecepatan angin yang dinormalisasi. Nilainya dibagi menjadi 67 (maks)
- santai: jumlah pengguna biasa
- terdaftar: jumlah pengguna terdaftar
- cnt: hitungan total sewa sepeda termasuk sepeda kasual dan terdaftar

============
Lisensi
============
Penggunaan kumpulan data ini dalam publikasi harus dikutip pada publikasi berikut:

[1] Fanaee-T, Hadi, dan Gama, Joao, "Pelabelan peristiwa yang menggabungkan detektor ansambel dan pengetahuan latar belakang", Kemajuan dalam Kecerdasan Buatan (2013): hlm. 1-15, Springer Berlin Heidelberg, doi:10.1007/s13748-013 -0040-3.

@artikel{
tahun={2013},
issn={2192-6352},
journal={Kemajuan dalam Kecerdasan Buatan},
doi={10.1007/s13748-013-0040-3},
judul={pelabelan ventilasi yang menggabungkan detektor ansambel dan pengetahuan latar belakang},
url={http://dx.doi.org/10.1007/s13748-013-0040-3},
penerbit={Springer Berlin Heidelberg},
kata kunci={Pelabelan peristiwa; Deteksi peristiwa; Pembelajaran ansambel; Latar belakang pengetahuan},
penulis={Fanaee-T, Hadi dan Gama, Joao},
halaman={1-15}
}

============
Kontak
============

Untuk informasi lebih lanjut mengenai dataset ini silakan menghubungi Hadi Fanaee-T (hadi.fanaee@fe.up.pt)