from typing import Counter


def study_schedule(permanence_period, target_time):
    try:
        count = 0
        if not (isinstance(target_time, int)):
            return None
        count = teste(permanence_period,  target_time, count)
        return count
    except TypeError:
        return None


def teste(permanence_period,  target_time, count):
    for index in permanence_period:
        if (index[0] <= target_time <= index[1]):
            count += 1
    return count
