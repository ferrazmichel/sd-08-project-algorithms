def study_schedule(permanence_period, target_time):
    count = 0
    for person in permanence_period:
        if not target_time or not person[0] or not person[1]:
            return None

        if target_time >= person[0] and target_time <= person[1]:
            count += 1
    return count
