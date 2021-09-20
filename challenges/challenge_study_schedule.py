def study_schedule(permanence_period, target_time):
    count = 0
    for person in permanence_period:
        if target_time >= person[0] and target_time <= person[1]:
            count += 1
    return count
