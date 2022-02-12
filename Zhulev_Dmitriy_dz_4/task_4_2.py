import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    work_str = response.text
    code = code.upper()
    
    if code not in work_str:    
        return None
    else:
        idx_code = work_str.find(code)
        idx_nom = work_str.find('Nominal', idx_code) + 8
        
        nominal = ''
        while work_str[idx_nom].isdigit():
            nominal += work_str[idx_nom]
            idx_nom += 1
        nominal = int(nominal)
        
        idx_val = work_str.find('Value', idx_nom) + 6
        
        result_value = ''
        while work_str[idx_val].isdigit() or work_str[idx_val] == ',':
            result_value += work_str[idx_val]
            idx_val += 1
        result_value = float((result_value).replace(',', '.'))
        
        return result_value


print(currency_rates("USD"))
print(currency_rates("eur"))
print(currency_rates("noname"))
    
