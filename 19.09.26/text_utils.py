# Решение задания 7

def load_data():
    return [3, 17, 8, 25, 6, 12, 25, 9, 14]

def filter_above(values, threshold=10):
    rez = []
    for i in values:
        if i > threshold:
            rez.append(i)
    return rez

def mean(values):
    """Среднее арифметическое."""
    return sum(values) / len(values)
