
# Javascript and AJAX

Yan C.

2106752464

## Questions

#### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Pada asynchronous programming, sistem bisa diupdate tanpa harus dijalankan ulang karena sistem
bisa multitasking, contohnya adalah web asyncrhonous. Berbeda dengan synchronous programming
dengan web yang harus di refresh untuk melihat perubahan.

#### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. 
#### Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Dalam paradigma Event-driven programming, program bergantung pada 'event' yang terjadi pada sistem 
seperti perubahan waktu, tombol yang diklik, hover, dan sebagainya. Pada tugas ini, contohnya adalah
saat tombol delete ditekan

#### Jelaskan penerapan asynchronous programming pada AJAX

Dengan AJAX, kita dapat mengubah html tanpa harus merubah file yang dapat mengharuskan kita refresh page.
Selain itu, request POST dan GET dapat dibuat sendirinya

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Pertama, setup url sehingga path merujuk ke view yang sesuai. Buat AJAX GET request.
Buat script pada ajax yang functionnya dapat mengembalikkan data dari json dalam bentuk
bootstrap Card.
Bergeser ke POST request, buat function yang dapat mensubmit data di form modal yang sudah kita buat.
Kemudian data dari form kita simpan ke database dan secara asynchronous membuat card baru.