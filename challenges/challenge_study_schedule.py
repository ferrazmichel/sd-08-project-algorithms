def study_schedule(permanence_period, target_time):
    student_count = 0

    try:
        for student_hours in permanence_period:
            if student_hours[0] <= target_time <= student_hours[1]:
                student_count += 1
    except TypeError:
        return None

    return student_count
