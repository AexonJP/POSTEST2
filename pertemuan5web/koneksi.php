<?php
    $conn = mysqli_connect("localhost", "root", "", "b2_21");

    if (!$conn) {
        die("Gagal terhubung ke database". mysqli_connect_eror());
    }
?>