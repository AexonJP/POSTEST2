<?php
require 'koneksi.php';

if (isset($_POST['tambah'])) {
    $nama = htmlspecialchars($_POST["nama"]);
    $nim = htmlspecialchars($_POST["nim"]);
    $kelas = htmlspecialchars($_POST["kelas"]);
    $prodi = htmlspecialchars($_POST["prodi"]);

    $sql = "INSERT INTO mahasiswa values('', '$nim', '$nama','$prodi' , '$kelas')";

    $result = mysqli_query($conn, $sql);

    if ( $result ) {
        echo "
          <script>
            alert('Data berhasil ditambah');
            document.location.href = 'index.php';
          </script>  
        ";
    } else {
        echo "
          <script>
            alert('Data berhasil ditambah');
            document.location.href = 'tambah.php';
          </script>  
        ";
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tambah data</title>
</head>
<body>
    <h1>Tambah Data</h1>
    <form action="" method="post">
        <label for="nim">Nim</label>
        <input type="number" name="nim" required> <br> <br>
        <label for="nama">Nama</label>
        <input type="text" name="nama" required> <br> <br>
        <label for="kelas">Kelas</label>
        <input type="text" name="kelas" required> <br> <br>
        <label for="prodi">Prodi</label>
        <input type="text" name="prodi" required> <br> <br>
        <button type="submit" name="tambah">Tambah</button>
    </form>
</body>
</html>