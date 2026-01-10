# TODO Напишите функцию find_common_participants
from os.path import split

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(a, b, c = ','):
    a = set(a.split(c))
    b = set(b.split(c))
    x = list(a.intersection(b))
    x.sort()
    return x


print(find_common_participants(a=participants_first_group, b=participants_second_group,c='|'))


# TODO Провеьте работу функции с разделителем отличным от запятой
