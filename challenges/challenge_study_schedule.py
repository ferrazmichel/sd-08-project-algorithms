def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    count = 0

    try:
        for student in permanence_period:
            if student[0] <= target_time <= student[1]:
                count += 1
    except TypeError:
        return None

    return count
# iteração no permanece_period que irá 'contar' a qtd de
# estudantes que tão consumindo o conteúdo baseado nas tuplas,
# que representam horário de entrada e saída do sistema.
# Verificar o teste do arquivo. Iteração feita nas tuplas
