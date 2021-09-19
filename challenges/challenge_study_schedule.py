def study_schedule(permanence_period, target_time):
    students_same_time = 0
    try:
        for student in permanence_period:
            if student[0] <= target_time <= student[1]:
                students_same_time += 1
    except TypeError:
        return None
    return students_same_time
