def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    target_time_occurrence = 0

    for login_time, logoff_time in permanence_period:
        if not (isinstance(login_time, int) and isinstance(logoff_time, int)):
            return None
        if login_time <= target_time <= logoff_time:
            target_time_occurrence += 1

    return target_time_occurrence
