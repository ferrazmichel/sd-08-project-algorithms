def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for student in permanence_period:
            if student[0] <= target_time and student[1] >= target_time:
                counter += 1
        return counter
    except TypeError:
        return None
