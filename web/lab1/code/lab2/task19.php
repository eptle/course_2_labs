<?php
function pyramid() {
    for($i = 1; $i <= 20; $i++) {
        echo str_repeat('x', $i) . "\n";
    }
}

pyramid();