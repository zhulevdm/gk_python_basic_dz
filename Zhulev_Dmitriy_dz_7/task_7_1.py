import os

with open('project_template.txt', 'r', encoding = 'utf-8') as fr:
    dir_root = fr.readline().rstrip('\n')
    if not os.path.exists(dir_root):
        os.mkdir(dir_root)
    for line in fr:
        sub_dir = os.path.join(dir_root , line)
        if not os.path.exists(sub_dir):
            os.makedirs(sub_dir)
