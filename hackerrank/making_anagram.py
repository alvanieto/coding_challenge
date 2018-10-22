def makeAnagram(a, b):
    a_dict = _build_dict(a)
    b_dict = _build_dict(b)
    replaces = 0
    for key, value in a_dict.items():
        if key in b_dict:
            if b_dict[key] != value:
                replaces += abs(b_dict[key] - value)
            b_dict.pop(key)
        else:
            replaces += value

    for value in b_dict.values():
        replaces += value
    return replaces


def _build_dict(data):
    res = {}
    for char_ in data:
        res.setdefault(char_, 0)
        res[char_] += 1
    return res
