def solution(a, b):
    short, long_ = (a, b) if len(a) < len(b) else (b, a)
    return '{short}{long_}{short}'.format(short=short, long_=long_)
