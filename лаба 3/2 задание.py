def find_common_participants(first_group,second_group, separator=","):
    first_list=first_group.split(separator)
    second_list=second_group.split(separator)



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(first_group, second_group, separator=","):
    first_list = [name.strip() for name in first_group.split(separator)]
    second_list = [name.strip() for name in second_group.split(separator)]
    return sorted(set(first_list) & set(second_list))
