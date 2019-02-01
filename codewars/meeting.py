def meeting(s):
    upper = [_parse_person(row) for row in s.split(';')]
    return ''.join('({}, {})'.format(*row) for row in sorted(upper))


def _parse_person(row):
    name, surname = row.split(':')
    return (surname.upper(), name.upper())
