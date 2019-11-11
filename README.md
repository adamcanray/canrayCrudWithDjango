## Membuat website CRUD dengan Django dan MySQL
Python Version: **3.7.0** </br>
Django Version: **2.2.7** </br>

Structure Files:
* **Env/** </br>
folder **Env** ini harus ada sebagai virtualenv. saya tidak meng-upload nya pada repo ini karena size yang lumayan hingga 109 MB(tergantung packages apasaja yang sudah terinstall). saya bisa membuat virtualenv dengan command berikut: ```python -m venv Env``` -- artinya kita ingin membuat sebuah virtualenv dengan nama folder-nya Env. pastikan virtual Env berada pada main folder(bisa ikuti langkah pada **0_catatan/1_membuat_project_django.txt**).
* **0_catatan/**
  * 0_project_target_time.txt -- adalah file yang berisi target saya dalam menyelesaikan project ini.
  * 1_membuat_project_django.txt -- file ini adalah langkah awal untuk membuat project django.
* **crudwithdjango/**
  * crudwithdjango/ </br>
    adalah folder project yang saya buat. untuk penjelasan detail mengenai fungsi dari file-file di dalam folder ini kamu bisa kunjungi repo ini [canrayLearnDjango](https:/github.com/adamcanray/canrayLearnDjango)
  * db.sqlite3 -- adalah file **database sqlite3** yang otomatis sudah terbuatketika kit amembuat project di django.
  * manage.py -- adalah file kunci yang untuk menjalankan testing, runserver dan semua yang kontrol pada project ada di file ini. contoh penggunaan: ```python manage.py runserver```
* 