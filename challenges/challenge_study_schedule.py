def study_schedule(permanence_period, target_time):
    count = 0

    if not target_time:
        return None

    for student in permanence_period:
        if not student[0] or not student[1]:
            return None

        if target_time >= student[0] and target_time <= student[1]:
            count += 1

    return count
    