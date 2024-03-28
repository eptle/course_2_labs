<?php
session_start();
if(false === isset($_SESSION['surname'], $_SESSION['name'])) {
    header('Location: /task2/task2.php');
    exit();
}
$name = $_SESSION['name'];
$surname = $_SESSION['surname'];
echo "<h1>Добро пожаловать в личный кабинет, $name $surname!</h1>";