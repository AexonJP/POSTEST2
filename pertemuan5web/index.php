<?php
require('koneksi.php');

$result = mysqli_query($conn, "SELECT * FROM mahasiswa");

$mahasiswa = [];

while ($row = mysqli_fetch_assoc($result)) {
    $mahasiswa[] = $row;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index</title>
</head>
<body>
    <h1>ini halaman index</h1>
    <button><a href="tambah.php">Tambah Data</a></button>
    <table>
        <tr>
            <td>No.</td>
            <td>NIM</td>
            <td>Nama</td>
            <td>Kelas</td>
            <td>Prodi</td>
            <td>Aksi</td>
        </tr>
        <?php $i = 1; foreach ($mahasiswa as $mhs): ?>
        <tr>
            <td> <?php echo $i; ?> </td>
            <td> <?php echo $mhs['nim']; ?> </td>
            <td> <?php echo $mhs['nama']; ?> </td>
            <td> <?php echo $mhs['kelas']; ?> </td>
            <td> <?php echo $mhs['prodi']; ?> </td>
            <td> <a href="ubah.php?id=<?php echo $mhs['id']; ?>">Edit</a> | <a href="hapus.php?id=<?php echo $mhs['id']; ?>" onclick="return confirm('Anda yakin ingin menghapus data ini?')" >Hapus</a> </td>
        </tr>
        <?php $i++; endforeach ?>
    </table>
</body>
</html>