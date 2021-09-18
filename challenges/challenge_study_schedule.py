def study_schedule(permanence_period, target_time):
    time_count = 0
    for (start, end) in permanence_period:
        try:
            if start <= target_time <= end:
                time_count += 1
        except TypeError:
            return None
    return time_count
