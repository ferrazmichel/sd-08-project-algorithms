def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if type(target_time) is not int:
        return None
    contador = 0
    for time_period in permanence_period:
        if type(time_period) is not int or type(time_period[1]) is not int:
            return None
        if time_period[0] == target_time or time_period[1] == target_time:
            contador += 1
        elif time_period[0] <= target_time and target_time <= time_period[1]:
            contador += 1
    if contador > 0:
        return contador
    return None


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
r = study_schedule(permanence_period, 1)
print(r)
