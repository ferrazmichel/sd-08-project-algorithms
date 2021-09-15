def study_schedule(permanence_period, target_time):
    try:
        count = 0
        if not (isinstance(target_time, int) and target_time >= 0):
            return None
        for index in permanence_period:
            if (index[0] <= target_time <= index[1]):
                count += 1
        return count
    except TypeError:
        return None
