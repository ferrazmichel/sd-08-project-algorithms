def study_schedule(permanence_period, target_time):
    """Função para identificar o horário com maior tráfego no site da escola"""
    if target_time is None:
        return None

    contador = 0

    for permanence in permanence_period:
        if permanence[0] is None or permanence[1] is None or \
          type(permanence[0]) != int or type(permanence[1]) != int:
            return None

        if permanence[0] <= target_time <= permanence[1]:
            contador += 1

    return contador
