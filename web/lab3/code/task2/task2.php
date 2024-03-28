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
        <form action="/task2/register2b.php" method="post">
            <label for="surname">Фамилия</label>
            <input type="text" name="surname" required >
            <br>
            <label for="name">Имя</label>
            <input type="text" name="name" required>
            <br>
            <input type="submit" value="Save">
        </form>
        <br>
        <a href="/task2/profile2b.php">Открыть личный кабинет</a>
    </div>

    <div>
        <h1>Task 2C</h1>
        <form action="/task2/register2c.php" method="post">
            <label for="name">Имя</label>
            <input type="text" name="name" required>
            <br>
            <label for="age">Возраст</label>
            <input type="text" name="age" required>
            <br>
            <label for="salary">Зарплата</label>
            <input type="text" name="salary" required>
            <br>
            <label for="phone_number">Номер телефона</label>
            <input type="text" name="phone_number" required>
            <br>
            <label for="totem">Тотемное животное</label>
            <input type="text" name="totem" required>
            <br>
            <input type="submit" value="Save">
        </form>
        <a href="/task2/profile2c.php">Открыть личный кабинет</a>
    </div>
</body>
</html>