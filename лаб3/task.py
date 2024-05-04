# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants (participants_first_group, participants_second_group, a =','):
    list1 = participants_first_group.split("|")
    list2 = participants_second_group.split("|")
    common = list(set(list1).intersection(list2))
    common.sort()
    return common
print(f"Общие участники: {find_common_participants(participants_first_group, participants_second_group, a =',')}")
# TODO Провеьте работу функции с разделителем отличным от запятой


