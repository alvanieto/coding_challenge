def find_uniq(data):
    base_num, is_end = calculate_base_num(*data[:3])
    if is_end:
        return base_num
    for num in data[3:]:
        if num != base_num:
            return num


def calculate_base_num(one, two, three):
    if one == two and one == three:
        return one, False
    if one == two and one != three:
        return three, True
    if one != two and one == three:
        return two, True
    if one != two:
        return one, True
