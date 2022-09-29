# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django
[Link to Herokuapp](https://tugasmvt.herokuapp.com/todolist/)

# Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
 CSRF token (Cross-Site Request Forgery Token) memberikan token acak yang bersifat unik untuk setiap sesi user. Token ini diperlukan untuk menangkal serangan CSRF yang memanfaatkan status user yang telah berhasil login. Serangan CSRF salah satunya adalah mengubah password user.

# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
 tentu Bisa, elemen <form> dapat dibuat manual, <form> adalah sebuah wrapper untuk beberapa field `<input>`.

# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

browser akan mengirim sebuah request POST dengan input yang telah dimasukan user setelah tombol submit ditekan. Request tersebut akan diproses oleh fungsi pada views.py, return yang diberikan disesuaikan apakaha valid (http akan meredirect sesuai dengan request) atau error (akan dimunculkan error message)

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

### 1) start app baru todolist
### 2) set installed app todolist ke settings.py
### 3) cocokkan url pattern ke urls.py
### 4) buat model dan views sesuai requirements di tugas
### 5) buat forms.py untuk melengkapi fungsi di views. Perlu diperhatikan juga beberapa fungsi yang hanya dapat dikases oleh user yang sudah login (loginrequired)
### 6) buat HTML yang dibutuhkan
### 7) check routing pattern di urks.py
### 8) push and deploy

:grin: