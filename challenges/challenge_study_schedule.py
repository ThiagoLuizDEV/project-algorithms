def study_schedule(permanence_period, target_time):

    if target_time is None:
        return None
    count = 0
    try:
        for index in permanence_period:
            initial_time, end_time = index
            if initial_time <= target_time <= end_time:
                count += 1
        return count
    except:
        return None

