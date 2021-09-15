def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for period in permanence_period:
            if target_time >= period[0] and target_time <= period[1]:
                count += 1
    except TypeError:
        return None
    return count
