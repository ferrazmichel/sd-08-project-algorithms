def study_schedule(permanence_period, target_time):
    counter = 0
    for moment in permanence_period:
        try:
            result = target_time >= moment[0] and target_time <= moment[1]
        except TypeError:
            return None
        else:
            if result:
                counter += 1
    return counter
