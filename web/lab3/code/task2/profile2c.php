<?php

session_start();
if (false === isset($_SESSION['person'])) {
    header('Location: /task2/task2.php');
    exit();
}
$data = $_SESSION['person'];

echo "<ul>";
foreach ($data as $value) {
    echo "<li>$value</li>\n";
}
echo "</ul>";