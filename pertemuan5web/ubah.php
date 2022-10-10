<?php
require 'koneksi.php';
$id = $_GET['id'];

$result = mysqli_query($conn, "SELECT * FROM mahasiswa WHERE id=$id");

$mahasiswa = [];

while ($row = mysqli_fetch_assoc($result)) {
    $mahasiswa[] = $row;
}

$mhs = $mahasiswa[0];

if (isset($_POST['tambah'])) {
    $nama = $_POST["nama"];
    $nim = $_POST["nim"];
    $kelas = $_POST["kelas"];
    $prodi = $_POST["prodi"];

    $sql = "UPDATE mahasiswa SET 
            nim = '$nim',
            nama = '$nama',
            kelas = '$kelas',
            prodi = '$prodi'
            WHERE id = '$id';
            ";

    $result = mysqli_query($conn, $sql);

    if ( $result ) {
        echo "
          <script>
            alert('Data berhasil diubah');
            document.location.href = 'index.php';
          </script>  
        ";
    } else {
        echo "
          <script>
            alert('Data gagal diubah');
            document.location.href = 'ubah.php';
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
    <title>Ubah data</title>
</head>
<body>
    <h1>Ubah Data</h1>
    <form action="" method="post">
        <input type="hidden" name="id" value="<?php echo $id; ?>">
        <label for="nim">Nim</label>
        <input type="number" name="nim" value="<?php echo $mhs['nim']; ?>"> <br> <br>
        <label for="nama">Nama</label>
        <input type="text" name="nama" value="<?php echo $mhs['nama']; ?>"> <br> <br>
        <label for="kelas">Kelas</label>
        <input type="text" name="kelas" value="<?php echo $mhs['kelas']; ?>"> <br> <br>
        <label for="prodi">Prodi</label>
        <input type="text" name="prodi" value="<?php echo $mhs['prodi']; ?>"> <br> <br>
        <button type="submit" name="tambah">Edit</button>
    </form>
</body>
</html>