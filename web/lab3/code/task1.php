<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>third laba</title>
</head>
<body>
    <?php
    echo '<h1>Task 1A</h1>';

    $str = 'ahb acb aeb aeeb adcb axeb';
    $regex1 = '/a..b/';
    preg_match_all($regex1, $str, $result);
    print_r($result);
    echo '<br>';
    #-----
    echo '<h1>Task 1B</h1>';

    $strWithNums = 'a1b2c3';
    $regex2 = '/[0-9]+/';
    $cube = function($match) {
        return $match[0] ** 3;
    };
    $strWithNums = preg_replace_callback($regex2, $cube, $strWithNums);
    print_r($strWithNums);
    ?>
</body>
</html>