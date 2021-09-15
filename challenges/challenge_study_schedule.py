def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if (target_time is None) or (permanence_period is None):
        return None
    cont = 0
    for tuple in permanence_period:
        if ((type(tuple[0]) != int) or type(tuple[1]) != int):
            return None
        if tuple[0] <= target_time <= tuple[1]:
            cont += 1
    return cont
