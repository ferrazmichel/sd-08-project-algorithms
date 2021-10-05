def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for cur in permanence_period:
            if(cur[0]) <= target_time <= cur[1]:
                count += 1
        return count
    except TypeError:
        return None
