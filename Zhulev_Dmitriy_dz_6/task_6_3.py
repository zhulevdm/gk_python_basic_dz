import sys
import json
import csv


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    users_list = [] 
    with open(path_users_file, newline='') as fr:  
        reader = csv.reader(fr)
        for row in reader:
            user = ' '.join(row)
            users_list.append(user)
        
    hobby_list = [] 
    with open(path_hobby_file, newline='') as fr:  
        reader = csv.reader(fr)
        for row in reader:
            hobby_list.append(row)
        
    if len(users_list) < len(hobby_list):
        sys.exit(1)

    if len(hobby_list) < len(users_list):
            diff = len(users_list) - len(hobby_list)
            while diff:
                hobby_list.append([None])
                diff -= 1

    dict_result = {}
    for key, val in zip(users_list, hobby_list):
        dict_result[key] = val

    return  dict_result


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
