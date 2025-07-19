<?php
require_once 'config.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    
    <title>Upload Foto</title>
    
    <link rel="stylesheet" href="styles.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
        <h2>Upload Foto</h2>
        
        <!-- input file untuk mengupload foto, di-hidden agar tidak terlihat -->
        <input type="file" id="fileInput" accept="image/*" style="display: none;">
        
        <!-- tombol untuk memilih foto dari galeri atau mengambil foto menggunakan kamera -->
        <div class="button-group">
            <button class="btn" id="galleryBtn">
                <span class="icon">📁</span> Pilih dari Galeri
            </button>
            <button class="btn" id="cameraBtn">
                <span class="icon">📷</span> Ambil Foto
            </button>
        </div>
        
        <!-- modal untuk mengambil foto menggunakan kamera -->
        <div id="cameraModal" class="modal">
            <div class="modal-content">
                <!-- tombol untuk menutup modal -->
                <span class="close">&times;</span>
                <h3>Ambil Foto</h3>
                <div class="camera-container">
                    <!-- video akan ditampilkan disini -->
                    <video id="video" autoplay playsinline></video>
                    <!-- canvas untuk menggambar gambar yang diambil -->
                    <canvas id="canvas" style="display: none;"></canvas>
                </div>
                <div class="camera-controls">
                    <!-- tombol untuk mengambil gambar -->
                    <button id="captureBtn" class="btn">Ambil Gambar</button>
                    <!-- tombol untuk mengulangi mengambil gambar -->
                    <button id="retakeBtn" class="btn" style="display: none;">Ulangi</button>
                    <!-- tombol untuk menggunakan foto yang diambil -->
                    <button id="usePhotoBtn" class="btn" style="display: none;">Gunakan Foto Ini</button>
                </div>
            </div>
        </div>
        
        <!-- preview foto yang di-upload -->
        <div id="preview" class="preview-container"></div>

    <script src="script.js"></script>
</body>
</html>
