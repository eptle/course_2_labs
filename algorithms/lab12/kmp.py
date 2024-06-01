def lps(pattern):
    lps = [0] * len(pattern)
    j = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp(text, pattern):
    if not pattern:
        return []
    lpsu = lps(pattern)
    i = 0
    j = 0
    matches = []
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == len(pattern):
                matches.append(i - j)
                j = lpsu[j - 1]
        else:
            if j != 0:
                j = lpsu[j - 1]
            else:
                i += 1
    return matches


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.readlines()
        text = "".join(text).replace('\n', '').lower()

    pattern = 'abc'
    #text = 'ascbabcabcacbabcabcabcsasbcabscabcbscbascbacabcscbcbxcmasbc'
    print(kmp(pattern, text))
