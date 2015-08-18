from datetime import datetime,timedelta


def convert(word):
    if 'second' in word:
        return 1
    if 'minute' in word:
        return 60
    if 'hour' in word:
        return 3600


def compute_ratio(text):
    ls = text.split()
    a = int(ls[0]) * convert(ls[1])
    b = int(ls[3]) * convert(ls[4])
    return float(b)/(a+b)


def broken_clock(starting_time, wrong_time, error_description):
    start = datetime.strptime(starting_time, '%H:%M:%S')
    wrong = datetime.strptime(wrong_time, '%H:%M:%S')
    wrong_delta = (wrong-start).total_seconds()
    delta = wrong_delta * compute_ratio(error_description)
    right = start + timedelta(seconds=delta)
    return right.strftime('%H:%M:%S')

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'
