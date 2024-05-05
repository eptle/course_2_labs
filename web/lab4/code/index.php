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
            $categories = ['cars', 'estates', 'appliances', 'animals', 'other'];
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
            $id = '1dkUQaSFdAO7aTBs-xz4-eef9mVIjPq32YRBSZhX2Lm8';
            $gid = 0;
            $csv = file_get_contents('https://docs.google.com/spreadsheets/d/'.$id.'/export?format=csv&gid='.$gid);
            $csv = explode("\r\n", $csv);
            $array = array_map('str_getcsv', $csv);
            foreach ($array as $row) {?>
                <tr>
                    <?php
                    foreach ($row as $item) {?>
                        <td><?php echo $item;?></td>
                        <?php
                    }?>
                </tr>
                <?php
            }
            ?>
        </tbody>
    </table>
</div>
</body>
</html>