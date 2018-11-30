def gemstones(data):
    return len(set(data[0]).intersection(*data[1:]))
