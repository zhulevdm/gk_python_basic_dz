import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'([A-Za-z0-9]+[._-])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if not re.fullmatch(RE_MAIL, email):
        msg = f'wrong email: {email}'
        raise ValueError(msg)
    result = {}
    result_key = ['username', 'domain']
    name_domain = re.split('@', email)
    for key, val in zip(result_key, name_domain):
        result[key] = val
    return result


if __name__ == '__main__':  
    email_parse('someone@geekbrains.ru')
    email_parse('dom.home.9889@yandex.ru')
    email_parse('sar-nan.2022@mail.ru')
    email_parse('sar-nan.2022@mail-com.ru')
    email_parse('someone@geekbrainsru')
