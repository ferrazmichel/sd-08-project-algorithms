def study_schedule(permanence_period, target_time):
    """Função para identificar o horário com maior tráfego no site da escola"""
    contador = 0
    try:
        for permanence in permanence_period:
            if permanence[0] <= target_time <= permanence[1]:
                contador += 1

        return contador
    except TypeError:
        return None
