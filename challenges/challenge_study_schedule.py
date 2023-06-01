def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for index in permanence_period:
            initial_time, end_time = index
            if initial_time <= target_time <= end_time:
                count += 1
        return count
    except TypeError:
        return None
