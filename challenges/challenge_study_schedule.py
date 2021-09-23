def study_schedule(permanence_period, target_time):
    amount = 0
    for low_index, high_index in permanence_period:
        try:
            if low_index <= target_time <= high_index:
                amount += 1
        except Exception:
            return None
    return amount
