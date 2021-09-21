def study_schedule(permanence_period, target_time):
    CONTADOR = 0
    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                CONTADOR += 1
    except TypeError:
        return None
    return CONTADOR
