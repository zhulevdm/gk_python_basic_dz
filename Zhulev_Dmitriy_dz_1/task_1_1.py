def convert_time(duration: int) -> str:
    days = duration // 86400
    hours = (duration - days * 86400) // 3600
    minutes = (duration - (days * 86400 + hours * 3600)) // 60
    seconds = duration - (days * 86400 + hours * 3600 + minutes * 60)

    if duration < 60:
        return f'{duration} сек'
    elif 60 <= duration < 3600:
        return f'{minutes} мин {seconds} сек'
    elif 3600 <= duration < 86400:
        return f'{hours} час {minutes} мин {seconds} сек'
    else:
        return f'{days} дн {hours} час {minutes} мин {seconds} сек'


duration = 400153
result = convert_time(duration)
print(result)