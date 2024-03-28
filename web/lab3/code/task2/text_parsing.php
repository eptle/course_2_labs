<?php
if(false === isset($_REQUEST['text-example'])) {
    header('Location: /forms.php');
    exit();
}

$text = $_REQUEST['text-example'];

echo "Текст: {$text}<br>";
echo 'Количество слов: ' . str_word_count($text) . '<br>';
echo 'Количество символов: ' . strlen($text);