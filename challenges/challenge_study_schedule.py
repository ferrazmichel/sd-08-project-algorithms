def study_schedule(permanence_period, target_time):
    counter = 0
    for moment in permanence_period:
        # if (
        #     moment[0] is None
        #     or moment[1] is None
        #     or not isinstance(moment[0], int)
        #     or not isinstance(moment[1], int)
        # ):
        #     return None
        # if target_time >= moment[0] and target_time <= moment[1]:
        try:
            result = target_time >= moment[0] and target_time <= moment[1]
        except TypeError:
            return None
        else:
            if result:
                counter += 1
    return counter
