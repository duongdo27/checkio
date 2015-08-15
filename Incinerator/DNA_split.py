def count_inversion(array):
    count = 0
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                count += 1
    return count


def golf(sequence, partition_number):
    ls = [sequence[i: i+partition_number] for i in range(0, len(sequence)-partition_number+1, partition_number)]
    ls.sort(key=count_inversion)
    return ''.join(ls)

golf("ACGTTGCAACGTAGCT", 4)