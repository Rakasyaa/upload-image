-- Membuat database untuk menyimpan foto yang diupload
CREATE DATABASE IF NOT EXISTS photo_upload;
USE photo_upload;

-- Membuat tabel untuk menyimpan informasi foto yang diupload
CREATE TABLE IF NOT EXISTS photos (
    -- id unik untuk setiap foto
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- nama file yang diupload
    filename VARCHAR(255) NOT NULL,
    -- path untuk menyimpan file yang diupload
    filepath VARCHAR(255) NOT NULL,
    -- waktu upload foto
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
