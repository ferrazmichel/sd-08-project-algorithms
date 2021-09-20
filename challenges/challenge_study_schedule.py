def study_schedule(permanence_period, target_time):
    """ Recebe:
            - permanence_period:
                * tupla que representa o período de permanência de uma pessoa
                  estudante no sistema, com seu horário de entrada e saída;
            - target_time:
                * variável que representa os horários testados.
        Retorna:
            - o número de estudantes estudando no mesmo horário;
            - None se em permanence_period houver alguma entrada inválida;
            - None se target_time recebe um valor vazio.  """
    count = 0
    try:
        for start, end in permanence_period:
            if start <= target_time <= end:
                count += 1
        return count
    except (TypeError, ValueError):
        return None

    """ Referência:
        Plantão em 15/09/2021 com Bux """
