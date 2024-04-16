<?php
function redirectToHomePage(){
    header('Location: /index.php');
    exit();
}

if (false === isset($_POST['email'], $_POST['category'], $_POST['title'], $_POST['description'])){
    redirectToHomePage();
    exit();
}
$email = $_POST['email'];
$category = $_POST['category'];
$title = $_POST['title'];
$description = $_POST['description'];

$filePath = "";
$directories = ['categories', "/$category", "/$email"];

foreach ($directories as $dir) {
    $filePath .= $dir;
    if (!is_dir($filePath)) {
        mkdir($filePath);
        chmod($filePath, 0777);
    }
}
$filePath .= "/$title.txt";
if (false === file_put_contents($filePath, $description)) {
    throw new Exception("Error while writing content to a file");
}
chmod($filePath, 0777);
redirectToHomePage();