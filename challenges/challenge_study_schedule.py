def study_schedule(permanence_period, target_time):
    counter = 0
    if not target_time or not permanence_period:
        return None
    for student in permanence_period:
        if student[0] <= target_time and student[1] >= target_time:
            counter += 1
    return counter
