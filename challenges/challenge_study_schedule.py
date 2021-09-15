def study_schedule(permanence_period, target_time):
    try:
        count = 0
        if not (isinstance(target_time, int) and target_time >= 0):
            return None
        for index in permanence_period:
            start_time = index[0]
            end_time = index[1]
            if (start_time <= target_time <= end_time):
                count += 1
        return count
    except TypeError:
        return None
