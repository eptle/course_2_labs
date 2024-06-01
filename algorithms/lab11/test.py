# худший O(n*m) средний и лучший O(n+m) n - длина текста, m- длина паттерна

# Строит таблицу переходов, которая показывает куда перейти
def transition_function(pattern, alphabet):
    length_pattern = len(pattern)
    tf = [[0] * len(alphabet) for _ in range(length_pattern + 1)] # список списков нулей
    tf[0][ord(pattern[0]) - ord('a')] = 1 # инициализация начального состояния
    x = 0 # хранит предыдущее состояние

    for i in range(1, length_pattern + 1):
        for j in range(len(alphabet)):
            tf[i][j] = tf[x][j]
        if i < length_pattern:
            tf[i][ord(pattern[i]) - ord('a')] = i + 1
            x = tf[x][ord(pattern[i]) - ord('a')]

    return tf

# По таблице переходов ищет в тексте образец
def search_pattern(text, pattern):
    alphabet = set(text)
    tf = transition_function(pattern, alphabet)

    text_length = len(text)
    length_pattern = len(pattern)
    pattern_positions = []

    state = 0
    for i in range(text_length):
        state = tf[state][ord(text[i]) - ord('a')]
        if state == length_pattern: # Если достигли конечного состояния автомата, значит рассматриваемая подстрока совпала с образцом
            pattern_positions.append(i - length_pattern + 1)

    return pattern_positions


text = "ababcababcabc"
pattern = "ababc"
positions = search_pattern(text, pattern)
print("Образец на позициях:", positions)