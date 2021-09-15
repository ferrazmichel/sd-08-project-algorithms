def validate_permanence_period(start_time, end_time):
    if (not isinstance(start_time, int) or not isinstance(end_time, int)):
        return False
    return True


def study_schedule(permanence_period, target_time):
    qty_of_students = 0

    if (target_time is None):
        return None

    for start_time, end_time in permanence_period:
        if (not validate_permanence_period(start_time, end_time)):
            return None

        if start_time <= target_time <= end_time:
            qty_of_students += 1

    return qty_of_students
