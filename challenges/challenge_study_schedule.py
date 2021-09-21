def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    count = 0
    for tuple in permanence_period:
        if isinstance(tuple[0], int) and isinstance(tuple[1], int):
            if tuple[0] <= target_time <= tuple[1]:
                count += 1
        else:
            return None

    return count
