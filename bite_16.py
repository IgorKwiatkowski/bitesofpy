from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    #
    # special_intervals = [100, 200, 300, 365, 400, 500, 600, 700, 800, 365*2]
    # special_intervals.sort()
    # for num in special_intervals:
    #     yield PYBITES_BORN + timedelta(days=num)

    days = 0
    while True:
        days += 1
        if days % 100 == 0 or days % 365 == 0:
            yield PYBITES_BORN + timedelta(days=num)