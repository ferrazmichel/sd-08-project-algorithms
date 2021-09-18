def study_schedule(permanence_period, target_time):

    try:
        count = 0
        for item in permanence_period:
            start_time = item[0]
            end_time = item[1]
            if item[0] <= target_time <= item[1]:
                count = count+1
        return count
    except TypeError:
        return None
