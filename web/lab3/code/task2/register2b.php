<?php
session_start();
if(true === isset($_POST['surname'], $_POST['name'])) {
    $_SESSION['surname'] = $_POST['surname'];
    $_SESSION['name'] = $_POST['name'];
}
header('Location: /task2/task2.php');
exit();