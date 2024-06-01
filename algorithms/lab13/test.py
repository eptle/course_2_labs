def preprocessor(pattern):
    pattern_len = len(pattern)
    d_dict = {i: 0 for i in pattern}
    d_dict[pattern[pattern_len-2]] = 1
    d_min = 2

    for i in range(pattern_len-2, -1, -1):
        if d_dict[pattern[i-1]] == 0:
            d_dict[pattern[i-1]] = d_min
        d_min += 1

    d_list = [0] * pattern_len
    for i in range(pattern_len):
        d_list[i] = d_dict[pattern[i]]

    return d_dict


def compare(piece, pattern):
    if len(piece) == len(pattern):
        for i in range(len(pattern)-1, -1, -1):
            if piece[i] != pattern[i]:
                return piece[i], pattern[i]
        else:
            return -1
    return False

def boyer_moore(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    steps = preprocessor(pattern)
    answer = list()
    i = 0
    while i <= text_len - pattern_len + 1:
        comparison = compare(text[i:i+pattern_len], pattern)
        if comparison == -1:
            answer.append(i)
            i += pattern_len
        elif comparison[0] not in steps:
            i += pattern_len
        else:
            i += min(steps[comparison[0]], steps[comparison[1]])
    return answer



if __name__ == "__main__":
    text = "gcatcGCAGAGAGtatacagtacg".upper()
    pattern = "GCAGAGAG".upper()
    print(list(pattern))
    print(boyer_moore(pattern, text))
