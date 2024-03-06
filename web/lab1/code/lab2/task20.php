<?php
$arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
$average = array_sum($arr) / count($arr);
echo $average . "\n";
#-----
echo array_sum(range(1, 100)) . "\n";
#-----
$arr = [1, 4, 9, 16, 25, 49];
$sqrtArr = array_map('sqrt', $arr);
foreach ($sqrtArr as $value) {
    echo $value, " ";
}
echo "\n";
#-----
$alphabet = array_combine(range('a', 'z'), range(1, 26));
#-----
$str = '1234567890';
$pairs = str_split($str, 2);
echo array_sum($pairs) . "\n";