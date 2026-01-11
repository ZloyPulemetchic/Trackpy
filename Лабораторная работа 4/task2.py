# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as csv_file:
        reader = csv.DictReader(csv_file)
        for a in reader:
            data.append(a)


    with open(OUTPUT_FILENAME, "w") as json.file:# TODO Сериализовать в файл с отступами равными 4
        json.dump(data, json.file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
