# TODO Напишите функцию find_common_participants


def find_common_participants(group1, group2, separator=','):
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)

    common_participants = set(participants1) & set(participants2)

    return sorted(common_participants)

group_a = "Иванов;Петров;Сидоров"
group_b = "Сидоров;Кузнецов;Иванов"

common = find_common_participants(group_a, group_b, separator=';')
print("Общие участники:", common)

# TODO Провеьте работу функции с разделителем отличным от запятой
