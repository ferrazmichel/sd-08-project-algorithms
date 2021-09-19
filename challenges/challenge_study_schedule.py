def study_schedule(permanence_period, target_time):
    counter = 0
    for start, end in permanence_period:
        try:
            if start <= target_time <= end:
                counter += 1
        except Exception:
            return None
    return counter
