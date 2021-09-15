def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    count = 0
    if target_time is None:
        # print('oi 2')
        return None
    for study_hour in permanence_period:
        try:
            is_true = study_hour[0] <= target_time <= study_hour[1]
            # print(count)
        except (ValueError, TypeError):
            return None
        count += is_true
    return count
