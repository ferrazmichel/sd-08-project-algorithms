def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    best_hour = 0
    for begin, end in permanence_period:
        if not (type(begin) == int and type(end) == int):
            return None
        if target_time >= begin and target_time <= end:
            best_hour = best_hour + 1
    return best_hour
