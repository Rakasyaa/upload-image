$(document).ready(function() {
    // Elements
    const fileInput = $('#fileInput');
    const galleryBtn = $('#galleryBtn');
    const cameraBtn = $('#cameraBtn');
    const preview = $('#preview');
    const cameraModal = $('#cameraModal');
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const captureBtn = $('#captureBtn');
    const retakeBtn = $('#retakeBtn');
    const usePhotoBtn = $('#usePhotoBtn');
    const closeBtn = $('.close');
    
    let currentFile = null;
    let stream = null;

    // Tombol untuk membuka gallery file
    galleryBtn.on('click', function() {
        fileInput.attr('capture', null);
        fileInput.trigger('click');
    });

    // Tombol untuk membuka kamera
    cameraBtn.on('click', function() {
        // Membuka modal kamera dan memulai kamera
        openCamera();
    });
    
    // Membuka modal kamera dan memulai kamera
    function openCamera() {
        cameraModal.css('display', 'flex');
        startCamera();
    }
    
    // Memulai kamera
    async function startCamera() {
        try {
            // Menghentikan stream yang ada
            if (stream) {
                stream.getTracks().forEach(track => track.stop());
            }
            
            // Mengambil stream dari kamera
            stream = await navigator.mediaDevices.getUserMedia({
                video: {
                    facingMode: 'environment', // Menggunakan kamera belakang
                    width: { ideal: 1920 },
                    height: { ideal: 1080 }
                },
                audio: false
            });
            
            // Menyetel video source
            video.srcObject = stream;
            video.play();
            
            // Menampilkan video dan menyembunyikan canvas
            video.style.display = 'block';
            canvas.style.display = 'none';
            
            // Menampilkan tombol capture dan menyembunyikan tombol lainnya
            captureBtn.show();
            retakeBtn.hide();
            usePhotoBtn.hide();
            
        } catch (err) {
            console.error('Error accessing camera:', err);
            alert('Tidak dapat mengakses kamera. Pastikan Anda memberikan izin akses kamera.');
            closeCamera();
        }
    }
    
    // Menangkap gambar
    captureBtn.on('click', function() {
        // Menyetel ukuran canvas untuk mencocokkan video
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        
        // Menggambar frame video ke canvas
        const context = canvas.getContext('2d');
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        // Menampilkan canvas dan menyembunyikan video
        video.style.display = 'none';
        canvas.style.display = 'block';
        
        // Menampilkan tombol retake dan use photo
        captureBtn.hide();
        retakeBtn.show();
        usePhotoBtn.show();
    });
    
    // Ulangi foto
    retakeBtn.on('click', function() {
        // Menampilkan video dan menyembunyikan canvas
        video.style.display = 'block';
        canvas.style.display = 'none';
        
        // Menampilkan tombol capture dan menyembunyikan tombol lainnya
        captureBtn.show();
        retakeBtn.hide();
        usePhotoBtn.hide();
    });
    
    // Menggunakan foto
    usePhotoBtn.on('click', function() {
        // Mengkonversi canvas menjadi blob
        canvas.toBlob(function(blob) {
            // Membuat file dari blob
            const file = new File([blob], 'camera-photo.jpg', {
                type: 'image/jpeg',
                lastModified: Date.now()
            });
            
            // Mengupload file
            uploadFile(file);
            
            // Menutup kamera
            closeCamera();
        }, 'image/jpeg', 0.9);
    });
    
    // Menutup modal kamera
    function closeCamera() {
        // Menghentikan semua stream video
        if (stream) {
            stream.getTracks().forEach(track => track.stop());
            stream = null;
        }
        
        // Menyembunyikan modal
        cameraModal.hide();
    }
    
    // Menutup modal saat mengklik tombol close
    closeBtn.on('click', closeCamera);
    
    // Menutup modal saat mengklik di luar modal content
    $(window).on('click', function(event) {
        if (event.target === cameraModal[0]) {
            closeCamera();
        }
    });

    // File input change handler
    fileInput.on('change', function(e) {
        if (e.target.files.length > 0) {
            currentFile = e.target.files[0];
            
            // Check if file is an image
            if (!currentFile.type.match('image.*')) {
                alert('Hanya file gambar yang diizinkan');
                return;
            }
            
            uploadFile(currentFile);
            
            // Reset file input
            $(this).val('');
        }
    });
// Fungsi upload file (tanpa error handling)
function uploadFile(file) {
    const formData = new FormData();
    formData.append('photo', file);

    $.ajax({
        url: 'upload.php',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        dataType: 'json',
        success: function(data) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const img = $('<img>', {
                    src: e.target.result,
                    class: 'preview-image',
                    alt: 'Uploaded'
                });
                const previewItem = $('<div>', { class: 'preview-item' });
                previewItem.append(img);
                preview.prepend(previewItem);
            };
            reader.readAsDataURL(file);
        }
    });
}

// Fungsi load image (tanpa error handling)
function loadImages() {
    $.ajax({
        url: 'get_images.php',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            preview.empty();
            data.images.forEach(function(image) {
                const img = new Image();
                img.src = image;
                img.className = 'preview-image';
                img.alt = 'Uploaded';
                preview.append(img);
            });
        }
    });
}

    // Initial load of existing images
    loadImages();
});