def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if not target_time:
        return None
    result = 0
    for student_in, student_out in permanence_period:
        if not isinstance(student_in, int) or not isinstance(student_out, int):
            return None
        if student_in <= target_time <= student_out:
            result += 1
    return result
