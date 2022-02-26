import os
import shutil

BASE_DIR = os.path.abspath('my_project')

dir_templ = os.path.join(BASE_DIR, 'templates')
if not os.path.exists(dir_templ):
        os.makedirs(dir_templ)

folder = []
for i in os.walk(BASE_DIR):
    folder.append(i)   

for address, dirs, files in folder:
    for my_file in files:
        file_path = os.path.join(address, my_file)
        if my_file.endswith('.html'):
            dir_src = os.path.dirname(file_path).split('/')[-1]
            file_src = os.path.basename(file_path)
            dir_dst = os.path.join(dir_templ, dir_src)
            if not os.path.exists(dir_dst):
                os.makedirs(dir_dst)
            if not os.path.exists(os.path.join(dir_dst, file_src)):
                shutil.copy2(file_path, os.path.join(dir_dst, file_src))
