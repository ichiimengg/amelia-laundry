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
