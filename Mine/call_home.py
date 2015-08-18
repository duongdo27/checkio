from math import ceil


def parse_data(call):
    ls = call.split()
    minute = ceil(int(ls[2])/60.0)
    return ls[0], minute


def compute_cost(minute):
    if minute <= 100:
        return minute
    else:
        return 100 + (minute-100)*2


def total_cost(calls):
    a = {}
    for call in calls:
        day, minute = parse_data(call)
        if day in a:
            a[day] += minute
        else:
            a[day] = minute
    return sum(map(compute_cost, a.values()))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost((u"2014-01-01 01:12:13 181",
                       u"2014-01-02 20:11:10 600",
                       u"2014-01-03 01:12:13 6009",
                       u"2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost((u"2014-02-05 01:00:00 1",
                       u"2014-02-05 02:00:00 1",
                       u"2014-02-05 03:00:00 1",
                       u"2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost((u"2014-02-05 01:00:00 60",
                       u"2014-02-05 02:00:00 60",
                       u"2014-02-05 03:00:00 60",
                       u"2014-02-05 04:00:00 6000")) == 106, "Precise calls"
