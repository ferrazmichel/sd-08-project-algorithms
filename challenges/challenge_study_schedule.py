def study_schedule(permanence_period, target_time):
    if target_time is None or target_time < 0 or target_time > 23:
        return None

    count = 0

    for student in permanence_period:
        if not isinstance(student[0], int) or not isinstance(student[1], int):
            return None
        if student[0] <= target_time <= student[1]:
            count = count + 1

    return count
