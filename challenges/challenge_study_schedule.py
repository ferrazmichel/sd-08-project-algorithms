def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    count = 0
    try:
        for time in permanence_period:
            if time[0] <= target_time <= time[1]:
                count += 1
    except TypeError:
        return None
    return count

# References
# https://panda.ime.usp.br/algoritmos/static/algoritmos/06-busca.html
# https://algoritmosempython.com.br/cursos/algoritmos-python/pesquisa-ordenacao/pesquisa-linear/
# https://pt.stackoverflow.com/questions/388284/algor%C3%ADtmo-de-busca-bin%C3%A1ria-em-python
# https://pt.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array
