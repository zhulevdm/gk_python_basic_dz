import os

folder = 'some_data'
cnt_100 = cnt_1000 = cnt_10000 = cnt_100000 = 0

for item in os.scandir(folder):
    if os.path.isfile(item):
        file_size = os.stat(item).st_size
        if file_size < 101:
            cnt_100 += 1
        elif file_size < 1001:
            cnt_1000 += 1
        elif file_size < 10001:
            cnt_10000 += 1
        else:
            cnt_100000 += 1

result_dict = {100:cnt_100, 1000:cnt_1000, 10000:cnt_10000, 100000:cnt_100000}
print(result_dict)
