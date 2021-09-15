def study_schedule(permanence_period, target_time):
    try:
        count = 0
        if (target_time == type(None)): return None
        for index in permanence_period:
            if (index[0] <= target_time <= index[1]):
                count += 1
        return count
    except TypeError:
        return None
