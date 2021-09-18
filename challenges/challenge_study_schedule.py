def study_schedule(permanence_period, target_time):
    student_count = 0
    try:
        for row in permanence_period:
            if row[0] <= target_time <= row[1]:
                student_count += 1
    except TypeError:
        return None
    return student_count
