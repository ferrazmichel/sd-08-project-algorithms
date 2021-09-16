def study_schedule(permanence_period, target_time):
    for tuple in permanence_period:       
        if not all(isinstance(n, int) for n in tuple):
            return None

    if not isinstance(target_time, int):
        return None

    times = []

    for login, logoff in permanence_period:
        for time in range(login, logoff +1):
            times.append(time)

    return times.count(target_time)

permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

# for tuple in permanence_period:       
#     print(all(isinstance(n, int) for n in tuple))
  