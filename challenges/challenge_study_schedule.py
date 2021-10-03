def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None

    number_of_students = 0
    for permanence in permanence_period:
        checkin, checkout = permanence
        if type(checkin) != int or type(checkout) != int:
            return None
        if checkin <= target_time <= checkout:
            number_of_students += 1
    return number_of_students
