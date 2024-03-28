<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div>
        <h1>Task 2A</h1>
        <form action="text_parsing.php" method="post">
            <label for="text-example">Введите текст</label>
            <br>
            <textarea name="text-example" cols="50" rows="5"></textarea>
            <br>
            <input type="submit" value="Отправить">
        </form>
    </div>

    <div>
        <h1>Task 2B</h1>
        <form action="/task2/register.php" method="post">
            <label for="surname">Фамилия</label>
            <input type="text" name="surname" required >
            <br>
            <label for="name">Имя</label>
            <input type="text" name="name" required>
            <br>
            <input type="submit" value="Save">
        </form>
        <br>
        <a href="/task2/profile.php">Открыть личный кабинет</a>
    </div>
</body>
</html>