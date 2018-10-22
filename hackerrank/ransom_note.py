def checkMagazine(magazine, note):
    magazine_dict = _build_dict(magazine)
    note_dict = _build_dict(note)
    for key, value in note_dict.items():
        if magazine_dict.get(key, 0) < value:
            return False
    return True


def _build_dict(data):
    res = {}
    for word in data.split():
        res.setdefault(word, 0)
        res[word] += 1
    return res
