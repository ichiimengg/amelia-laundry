# Amelia Laundry – Web Application (Django)

Amelia Laundry adalah aplikasi web berbasis Django yang dibuat untuk mengelola proses laundry secara digital.  
Sistem ini memiliki tiga jenis pengguna, yaitu Admin, Customer, dan Driver.  
Setiap pengguna memiliki tampilan dashboard dan fitur yang berbeda sesuai dengan kebutuhan operasional.

---

## 1. Fitur Utama

### 1.1 Login & Registrasi
- Login dengan role (Admin, Customer, Driver)
- Registrasi pengguna baru (Customer)
- Validasi data pengguna

### 1.2 Admin Dashboard
- Melihat seluruh pesanan
- Mengelola data customer dan driver
- Melihat laporan transaksi
- Mengupdate status pesanan
- Menampilkan total pendapatan

### 1.3 Customer Dashboard
- Membuat pesanan laundry
- Melihat status pesanan
- Melihat estimasi harga berdasarkan layanan

### 1.4 Driver Dashboard
- Melihat pesanan yang harus diambil/diantar
- Mengubah status pesanan
- Menjalankan proses pengiriman

---

## 2. Penerapan Object-Oriented Programming (OOP)

Sistem ini menggunakan konsep OOP untuk mengatur role pengguna dan proses bisnis.

### 2.1 Superclass: BaseRole  
File: `main/user_roles.py`

```python
class BaseRole:
    def __init__(self, username):
        self.username = username

    def get_role_name(self):
        return "Base"

    def get_display_name(self):
        return self.username.capitalize()
Superclass ini digunakan untuk mendefinisikan atribut dan method umum bagi semua role.

2.2 Subclass: AdminRole, CustomerRole, DriverRole
python
Copy code
class AdminRole(BaseRole):
    def get_role_name(self):
        return "Admin"

class CustomerRole(BaseRole):
    def get_role_name(self):
        return "Customer"

class DriverRole(BaseRole):
    def get_role_name(self):
        return "Driver"
Setiap subclass melakukan override terhadap method get_role_name().
Penerapan ini menunjukkan konsep inheritance dan polymorphism.

2.3 Method Bisnis pada Model
File: main/models.py

python
Copy code
@property
def total_price(self):
    if self.service_type == "express":
        return self.weight_kg * 8000
    elif self.service_type == "kilat":
        return self.weight_kg * 10000
    return self.weight_kg * 6000
Method ini digunakan untuk menghitung total biaya laundry berdasarkan:

berat cucian

jenis layanan

3. Cara Instalasi dan Menjalankan Aplikasi
3.1 Clone Repository
bash
Copy code
git clone https://github.com/USERNAME/NAMA-REPO.git
3.2 Masuk ke Direktori Project
bash
Copy code
cd NAMA-REPO
3.3 Install Dependencies
Jika memiliki file requirements.txt:

css
Copy code
pip install -r requirements.txt
Jika tidak:

nginx
Copy code
pip install django
3.4 Migrasi Database
nginx
Copy code
python manage.py migrate
3.5 Membuat Superuser (Admin)
nginx
Copy code
python manage.py createsuperuser
3.6 Menjalankan Server
nginx
Copy code
python manage.py runserver
Aplikasi dapat diakses melalui:

cpp
Copy code
http://127.0.0.1:8000/
4. Struktur Direktori
css
Copy code
jemput_antar/
│
├── main/
│   ├── templates/
│   ├── user_roles.py
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│
├── jemput_antar/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── db.sqlite3
5. Teknologi yang Digunakan
Python 3.x

Django 4.x

HTML & CSS

Bootstrap (opsional)
