def study_schedule(permanence_period, target_time):
    count = 0
    if target_time is None:
        return None
    for student in permanence_period:
        if type(student[0]) is not int or type(student[1]) is not int:
            return None
        if student[0] <= target_time <= student[1]:
            count += 1

    return count
