<?php
session_start();
if(true === isset($_POST['name'], $_POST['age'], $_POST['salary'], $_POST['phone_number'], $_POST['totem'])) {
    $_SESSION['person'] = [$_POST['name'], $_POST['age'], $_POST['salary'], $_POST['phone_number'], $_POST['totem']];
}
header('Location: /task2/task2.php');
exit();