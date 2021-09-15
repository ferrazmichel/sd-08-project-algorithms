def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is not None:
        for moment in range(len(permanence_period)):
            if (
                permanence_period[moment][0] is None
                or permanence_period[moment][1] is None or
                not isinstance(permanence_period[moment][0], int) or
                not isinstance(permanence_period[moment][1], int)
            ):
                return None
            if (
                target_time >= permanence_period[moment][0]
                and target_time <= permanence_period[moment][1]
            ):
                counter += 1
        return counter
