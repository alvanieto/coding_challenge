def format_words(words):
    real_words = [word for word in words if word] if words else []
    res = ''
    if len(real_words) == 1:
        res = real_words[0]
    elif len(real_words) > 1:
        res = '{} and {}'.format(', '.join(real_words[:-1]), real_words[-1])
    return res
