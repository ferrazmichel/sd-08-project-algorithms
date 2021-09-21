def study_schedule(permanence_period, target_time):
    number_of_students = 0
    for arrive_time, leave_time in permanence_period:
        try:
            if arrive_time <= target_time <= leave_time:
                number_of_students += 1
        except Exception:
            return None
    return number_of_students
