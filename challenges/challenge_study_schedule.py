def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    count = 0

    for tup in permanence_period:
        if not tup[0] or not tup[1]:
            return None

        if target_time >= tup[0] and target_time <= tup[1]:
            count += 1

    return count
