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
            $categories = ['cars', 'books', 'other'];
            foreach ($categories as $category) {?>
                <option value=<?php echo $category;?>><?php
                    echo $category;?></option><?php }?>
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
            $host = 'db';
            $user = 'root';
            $password = 'helloworld';
            $database = 'web';

            $mysqli = new mysqli($host, $user, $password, $database);

            $link = $mysqli->query("SELECT email, category, title, description FROM ad");
            while ($row = $link->fetch_assoc()) {?>
                <tr>
                    <?php
                    foreach(['email', 'category', 'title', 'description'] as $item) {?>
                        <td><?php echo $row[$item];?></td>
                        <?php
                    }?>
                </tr>
                <?php
            }
            $link->close();
            $mysqli->close();
            ?>
        </tbody>
    </table>
</div>
</body>
</html>