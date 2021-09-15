def study_schedule(permanence_period, target_time):
    """ Faça o código aqui.   Horário tem a maior
    quantidade de pessoas acessando o conteúdo da
    plataforma ao mesmo tempo"""
    if not target_time or target_time != int:
        return None
    for index in range(len(permanence_period)):
        start_time = permanence_period[index][0]
        end_time = permanence_period[index][1]
        if start_time <= target_time <= end_time:
            return target_time
