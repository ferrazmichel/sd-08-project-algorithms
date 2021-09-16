def study_schedule(permanence_period, target_time):
    try:
        times_shown = 0
        for i in permanence_period:
            if i[0] <= target_time <= i[1]: times_shown += 1
        return times_shown
    except:
        return None
    