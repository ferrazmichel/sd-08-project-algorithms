def study_schedule(permanence_period, target_time):
    students_qntty = 0

    for start_time, end_time in permanence_period:
        try:
            if target_time >= start_time and target_time <= end_time:
                students_qntty += 1
        except Exception:
            return None
    return students_qntty