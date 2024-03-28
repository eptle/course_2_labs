<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Avito</title>
</head>
<body>
<div id="form">
    <form action="save.php" method="post">
        <label for="email">Email</label>
        <input type="email" name="email" required>
        <br>
        <label for="category">Выберите категорию</label>
        <select name="category" required>
            <?php
            $categories = scandir('./categories');
            foreach ($categories as $value) {
                if ($value != '.' and $value != '..')
                {
                    echo "<option value=\"$value\">$value</option>";
                }
            }
            ?>
        </select>
        <br>
        <label for="title">Заголовок</label>
        <input type="text" name="title" required>
        <br>
        <label for="description">Описание товара</label>
        <br>
        <textarea rows="5" cols="50", name="description"></textarea>
        <br>
        <input type="submit" value="Опубликовать">
    </form>
    <br>
</div>

<div id="list">
    <table border="1">
        <thead>
            <th>Email</th>
            <th>Категория</th>
            <th>Заголовок</th>
            <th>Описание</th>
        </thead>
        <tbody>
            <?php
            for($i = 2; $i < count($categories); $i++) {
                $category = $categories[$i];
                $emails = scandir("./categories/{$category}");

                for($j = 2; $j < count($emails); $j++) {
                    $email = $emails[$j];
                    $items = scandir("./categories/{$category}/{$email}");
                    for($k = 2; $k < count($items); $k++) {
                        $title = $items[$k];
                        $description = file_get_contents("./categories/{$category}/{$email}/{$title}");
                        $categoryDisplay = $category;
                        $formatTitle = substr($title, 0, strlen($title) - 4);

                        echo "<tr>";
                        echo "<td>$email</td>";
                        echo "<td>$categoryDisplay</td>";
                        echo "<td>$formatTitle</td>";
                        echo "<td>$description</td>";
                        echo "</tr>";
                    }
                }
            }
            ?>
        </tbody>
    </table>
</div>
</body>
</html>