data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(*args):
    sum_ = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            sum_ += arg
        elif isinstance(arg, str):
            sum_ += len(arg)
        elif isinstance(arg, (list, tuple)):
            sum_ += calculate_structure_sum(*arg)
        elif isinstance(arg, dict):
            sum_ += calculate_structure_sum(*arg.items())
        if isinstance(arg, set):
            sum_ += calculate_structure_sum(*arg)
    return sum_


result = calculate_structure_sum(data_structure)
print(result)