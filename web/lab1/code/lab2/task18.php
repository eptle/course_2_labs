<?php
function isMoreThan10(float $a, float $b) {
    return $a + $b > 10;
}
echo isMoreThan10(0, 1) . "\n";
#-----
function isEqual(float $a, float $b) {
    return $a === $b;
}

echo isEqual(1, 1) . "\n";
#-----
$test = 0;
if ($test == 0) {
    echo 'верно' . "\n";
}

echo $test == 0 ? 'верно' : '';
echo "\n";
#-----
$age = 99;

if (10 <= $age and $age <= 99) {
    if ($age % 10 + intdiv($age, 10) > 9) {
        echo 'сумма цифр двузначна' . "\n";
    }
    else {
        echo 'сумма цифр однозначна' . "\n";
    }
}
else {
    echo 'число не находится в диапазоне :(' . "\n";
}
#-----
$arr = [1, 2, 3];
if (count($arr) == 3) {
    echo array_sum($arr), "\n";
}
else {
    echo 'В массиве не 3 элемента' . "\n";
}