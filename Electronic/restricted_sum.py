def add_recursive(data, acc):
    if len(data) == 0:
        return acc
    return add_recursive(data[1:], acc+data[0])

def checkio(data):
    return add_recursive(data, 0)