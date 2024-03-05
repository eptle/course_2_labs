<?php
function printStringReturnNumber() {
    echo "hello world\n";
    return 12;
}

$myNum = printStringReturnNumber();
echo $myNum . "\n";