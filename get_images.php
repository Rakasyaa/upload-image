<?php
    // Koneksi ke database
    require_once 'config.php';   
    
    // Query untuk mengambil semua path file foto dari database
    $sql = "SELECT filepath FROM photos ORDER BY uploaded_at DESC";
    $result = $conn->query($sql);

    // Variable untuk menyimpan array path file foto
    $images = [];
    if ($result->num_rows > 0) {
        // Looping untuk mengambil setiap baris dari hasil query
        while ($row = $result->fetch_assoc()) {
            // Jika path file foto tidak kosong, masukkan ke array $images
            if (!empty($row['filepath'])) {
                $images[] = $row['filepath'];
            }
        }
    }
    
    // Buatkan response yang berisi array path file foto dan status success
    $response = [
        'success' => true,
        'images' => $images
    ];
    
    // Encode response menjadi format json dan kirimkan ke client
    echo json_encode($response);
?>
