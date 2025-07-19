# Aplikasi Upload Foto Sederhana

Aplikasi web sederhana untuk mengunggah dan melihat foto menggunakan PHP, MySQL, dan jQuery. Aplikasi ini memungkinkan pengguna untuk mengunggah foto baik dari galeri maupun langsung dari kamera perangkat.

## Persyaratan Sistem

1. XAMPP (Termasuk Apache, MySQL, dan PHP)
2. Browser web modern (Chrome, Firefox, Edge, dll.)
3. Koneksi internet (hanya untuk mengunduh file yang diperlukan)

## Panduan Instalasi

### 1. Instal XAMPP

1. Unduh XAMPP dari [situs resmi Apache Friends](https://www.apachefriends.org/download.html)
2. Jalankan file instalasi dan ikuti petunjuknya
3. Pastikan untuk menginstal komponen Apache, MySQL, dan PHP
4. Selesai instalasi, jalankan XAMPP Control Panel

### 2. Menyiapkan Database

1. Buka browser dan buka [phpMyAdmin](http://localhost/phpmyadmin)
2. Klik "New" di sidebar kiri untuk membuat database baru
3. Beri nama database: `photo_upload`
4. Klik tombol "Create"
5. Setelah database dibuat, klik pada tab "SQL"
6. Salin dan tempel kode SQL berikut, lalu klik "Go":

```sql
CREATE TABLE photos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    filepath VARCHAR(255) NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3. Menyiapkan File Aplikasi

1. Salin folder `upload image` ke dalam direktori `C:\xampp\htdocs\`
2. Buka folder `upload image` di komputer Anda
3. Buka file `config.php` dengan teks editor (seperti Notepad++ atau Visual Studio Code)
4. Pastikan pengaturan koneksi database sudah benar (biasanya tidak perlu diubah jika menggunakan pengaturan default XAMPP):

```php
$conn = new mysqli('localhost', 'root', '', 'photo_upload');
```

5. Simpan file tersebut

### 4. Membuat Folder Uploads

1. Di dalam folder `upload image`, buat folder baru bernama `uploads`
2. Klik kanan pada folder `uploads`
3. Pilih "Properties"
4. Pada tab "Security", klik "Edit..."
5. Klik "Add..."
6. Ketik "Everyone" dan klik "Check Names", lalu "OK"
7. Centang "Full control" pada kolom "Allow"
8. Klik "Apply" dan "OK"

### 5. Menjalankan Aplikasi

1. Pastikan Apache dan MySQL berjalan di XAMPP Control Panel
2. Buka browser dan kunjungi: [http://localhost/upload%20image/](http://localhost/upload%20image/)
3. Aplikasi siap digunakan!

## Cara Menggunakan

1. **Mengunggah Foto dari Galeri**:
   - Klik tombol "Pilih dari Galeri"
   - Pilih foto yang ingin diunggah
   - Klik "Open"

2. **Mengambil Foto dengan Kamera**:
   - Klik tombol "Ambil dengan Kamera"
   - Izinkan akses kamera jika diminta
   - Arahkan kamera dan klik "Ambil Gambar"
   - Jika sudah pas, klik "Gunakan Foto Ini"

## Troubleshooting

1. **Tidak bisa mengunggah foto**:
   - Pastikan folder `uploads` memiliki izin yang benar
   - Cek kapasitas penyimpanan server
   - Pastikan ukuran file tidak melebihi batas upload PHP (biasanya 2MB)

2. **Koneksi database gagal**:
   - Pastikan MySQL berjalan di XAMPP Control Panel
   - Periksa pengaturan di `config.php`
   - Pastikan database `photo_pload` sudah dibuat

3. **Kamera tidak berfungsi**:
   - Pastikan browser mendukung WebRTC
   - Pastikan sudah mengizinkan akses kamera
   - Coba gunakan browser yang berbeda

## Dukungan

Jika Anda menemui masalah, silakan buat issue baru di repositori ini atau hubungi administrator sistem Anda.

---

Dibuat dengan ❤️ untuk memudahkan pengunggahan foto secara sederhana dan efisien.
