def study_schedule(permanence_period, target_time):
    sum = 0
    if (not target_time):
        return None
    else:
        for period in permanence_period:
            if type(period[0]) != int or type(period[1]) != int:
                return None
            if period[0] <= target_time <= period[1]:
                sum += 1

        return sum
