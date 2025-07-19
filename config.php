<?php
// Koneksi ke database
// Membuat koneksi ke database dengan nama 'photo_upload'
// yang ada di localhost dengan username 'root' dan password kosong
$conn = new mysqli('localhost', 'root', '', 'photo_upload');

// Jika terjadi error saat koneksi, maka akan menampilkan error-nya
if ($conn->connect_error) {
    die("Koneksi gagal: " . $conn->connect_error);
}
?>
