# написати функцію stat, яка отримує масив цілих чисел, а повертає масив,
# [total_amount, unique_amount, once_occure_amount, [[max_occurance_elements], max_occurance]]

def stat(some_array):
    # (1) - Total amount of received integers.
    total_amount = len(some_array)

    # (2) - Total amount of different values the array has.
    unique_amount = len(set(some_array))

    # (3) - Total amount of values that occur only once.
    once_occure_amount = sum(1 for num in some_array if some_array.count(num) < 2)

    # (4) and (5) both in a list
    # (4) - It is (or they are) the element(s) that has (or have) the maximum occurrence.
    # If there are more than one, the elements should be sorted (by their value obviously)
    max_occurance_elements =

    # (5) - Maximum occurrence of the integer(s)
    max_occurance =

    return [
        total_amount,
        unique_amount,
        once_occure_amount,
        [[max_occurance_elements], max_occurance],
    ]
