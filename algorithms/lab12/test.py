def preprocessor(pattern):
    pattern_len = len(pattern)
    pi = {''.join(pattern[0:i+1]): 0 for i in range(0, pattern_len)}
    for word in pi.keys():
        if len(word) == 0:
            continue
        else:
            word_len = len(word)
            prefixes = set()
            suffixes = set()
            for prefix in range(1, word_len):
                prefixes.add(word[:prefix])
                suffixes.add(word[prefix:])
            equals = prefixes & suffixes
            if equals:
                pi[word] = len(max(equals))
            else:
                pi[word] = 0
    return list(pi.values())


def kmp(pattern, text):
    if not pattern:
        return []
    pi = preprocessor(pattern)
    i = 0  # Индекс для текста
    j = 0  # Индекс для паттерна
    answer = []
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == len(pattern):
                answer.append(i - j)
                j = pi[j - 1]
        else:
            if j != 0:
                j = pi[j - 1]
            else:
                i += 1


    return answer


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.readlines()
        text = "".join(text).replace('\n', '').lower()

    pattern = 'abcabd'
    text = 'abcabcbacbaaabcabd'
    print(kmp(pattern, text))
