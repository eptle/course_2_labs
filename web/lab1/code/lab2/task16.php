<?php
function increaseEnthusiasm(string $str) {
    return $str . '!';
}
echo increaseEnthusiasm('Hello world') . "\n";
#-----
function repeatThreeTimes(string $str) {
    return str_repeat($str, 3);
}
echo repeatThreeTimes(strrev('hello world')) . "\n";
echo increaseEnthusiasm(repeatThreeTimes('Что здесь происходит?')) . "\n";
#-----
function cut(string $str, int $len = 10) {
    return substr($str, 0, $len);
}
echo cut('hello world', 4) . "\n";
#-----
$arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
function recursiveOut(array $arr) {
    if (count($arr) > 1) {
        recursiveOut(array_slice($arr, 0, -1));
    }
    echo end($arr) . ' ';
}
echo recursiveOut($arr) . "\n";
#-----
$num = 999999;
function sumOfNum($num) {
    $temp = $num;
    $sum = 0;
    while ($temp > 0) {
        $sum += $temp % 10;
        $temp = intdiv($temp, 10);
    }
    if ($sum < 10) {
        return $sum;
    }
    else {
        return sumOfNum($sum);
    }
}
echo sumOfNum($num) . "\n";
#-----