<?php
// Koneksi ke database
require_once 'config.php';

// Set type respon ke json
header('Content-Type: application/json');

// Ambil file yang diupload
$file = $_FILES['photo'];

// Ambil ekstensi file (misal: .jpg, .png, dst)
$fileExtension = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));

// Generate nama file yang unik
$filename = uniqid() . '.' . $fileExtension;
// Path untuk menyimpan file yang diupload
$targetPath = 'uploads/' . $filename;

// Pindahkan file yang diupload ke path yang telah ditentukan
move_uploaded_file($file['tmp_name'], $targetPath);

// Buatkan query untuk menyimpan nama file dan path ke database
$stmt = $conn->prepare("INSERT INTO photos (filename, filepath) VALUES (?, ?)");
// Jika gagal, maka tampilkan error
if (!$stmt) {
    throw new Exception('Database prepare failed: ' . $conn->error);
}

// Bind parameter untuk nama file dan path
$stmt->bind_param("ss", $filename, $targetPath);

// Jalankan query
if (!$stmt->execute()) {
    throw new Exception('Database execute failed: ' . $stmt->error);
}

// Buatkan response yang berisi nama file dan path
echo json_encode([
    'success' => true,
    'filename' => $filename,
    'filepath' => $targetPath
]);

// Tutup koneksi statement
if (isset($stmt)) {
    $stmt->close();
}
?>
