# TODO решите задачу
import json
import os
def task() -> float:
    script_dir = os.getcwd()
    file_path = os.path.join(script_dir, 'input.json')

    with open(file_path) as json_file:
        data = json.load(json_file)
        total = sum(item.get("score") * item.get("weight") for item in data)
        return round(total, 3)






print(task())
