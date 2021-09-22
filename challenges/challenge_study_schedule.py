def study_schedule(permanence_period, target_time):
    '''
    Receive a list of tuples with the times of arrive
    and leave of the platform.

    Returns how many students were present in the target time.

    If target time is null or if permanence_period list
    has invalid time, returns None
    '''
    if target_time is None:
        return None
    counter = 0
    for times in permanence_period:
        if any(not isinstance(time, int) for time in times):
            return None
        elif times[0] <= target_time <= times[1]:
            counter += 1
    return counter
