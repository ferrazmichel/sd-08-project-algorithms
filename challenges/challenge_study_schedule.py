def study_schedule(permanence_period, target_time):
    if not target_time: 
        return None
    amount = 0
    for period in permanence_period:
        if target_time >= period[0] and target_time <= period[1]:
            amount += 1
    return amount
