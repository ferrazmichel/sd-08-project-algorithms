def study_schedule(permanence_period, target_time):
    count = 0
    for (enter, leave) in permanence_period:
        try:
            if enter <= target_time <= leave:
                count += 1
        except TypeError:
            return None
    return count
