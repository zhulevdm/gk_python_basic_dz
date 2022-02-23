def get_parse_attrs(line: str) -> tuple:
    """Парсит строку и возвращает строку '<remote_addr>'"""
    str_to_list = line.split()
    return  (str_to_list[0])


list_out_ip = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out_ip.append(get_parse_attrs(line))

set_ip = set(list_out_ip)

spamer = ''
cnt = 0
for ip in set_ip:
    i = list_out_ip.count(ip)
    if i > cnt:
        cnt = i
        spamer = ip

print(f'С адреса: {spamer} было произведено {cnt} запросов')
