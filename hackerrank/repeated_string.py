def repeatedString(s, n):
    return s.count('a') * int(n / len(s)) + s[:n % len(s)].count('a')
