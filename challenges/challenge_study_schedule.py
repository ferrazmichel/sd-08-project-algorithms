
def study_schedule(permanence_period, target_time):
    counter = 0

    try:
        for value, element in permanence_period:
            if value < target_time and target_time < element:
                counter += 1
        return counter
    except TypeError:
        return None
