import functools

def rabin_karp(text, pattern):
    BASE = 33
    pattern_len = len(pattern)
    text_hash = functools.reduce(lambda h, c: h * BASE + ord(c), text[:pattern_len], 0)
    print(text_hash)
    st_hash = functools.reduce(lambda h, c: h * BASE + ord(c), pattern, 0)
    print(st_hash)
    power_st = BASE**(pattern_len - 1)
    for i in range(pattern_len, len(text)):
        if text_hash == st_hash and text[i - pattern_len:i] == pattern:
            return i - pattern_len
        text_hash -= ord(text[i - pattern_len]) * power_st
        text_hash = text_hash * BASE + ord(text[i])
    if text_hash == st_hash and text[-pattern_len:] == pattern:
        return len(text) - pattern_len
    return -1


if __name__ == '__main__':
    text = "ACDBDCABCADBCBCDABCDAB"
    pattern = "ABC"
    print(rabin_karp(text, pattern))
