def quick_sort(param):
    if len(param) <= 1:
        return param
    if len(param) == 0:
        return []

    pivot_value = param[len(param) // 2]
    smaller = [index for index in param if index < pivot_value]
    equal = [index for index in param if index == pivot_value]
    bigger = [index for index in param if index > pivot_value]

    return quick_sort(smaller) + equal + quick_sort(bigger)


def is_anagram(first_string, second_string):
    first = ''.join(quick_sort(first_string.lower()))
    second = ''.join(quick_sort(second_string.lower()))
    if len(first) == 0 or len(second) == 0:
        return (first, second, False)
    boolean = first == second

    return (first, second, boolean)
