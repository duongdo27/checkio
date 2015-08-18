def flat_list(array):
    result = []
    for element in array:
        if type(element) == list:
            result += flat_list(element)
        else:
            result.append(element)
    return result


print flat_list([1, [2, 2, 2], 4])
print flat_list([-1, [1, [-2], 1], -1])