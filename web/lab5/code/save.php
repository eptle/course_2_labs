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

$host = 'db';
$user = 'root';
$password = 'helloworld';
$database = 'web';

$mysqli = new mysqli($host, $user, $password, $database);

$mysqli->query(sprintf("INSERT INTO ad (email, category, title, description) VALUES ('%s', '%s', '%s', '%s');", $email, $category, $title, $description));
redirectToHomePage();