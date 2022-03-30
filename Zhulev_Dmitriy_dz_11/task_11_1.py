class Date:

    def __init__(self, full_date: str):
        self.full_date = full_date
        
    @classmethod
    def transform_date(cls, string_date):
        day, month, year = map(int, string_date.split('-'))
        return day, month, year
    
    @staticmethod
    def valid_date(string_date):
        day, month, year = map(int, string_date.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and year <= 3000 #Думаю, дальше 3000 года заглядывать не будем )))

date_1 = Date('01-02-2022')

print(date_1.transform_date('01-02-2022'))
print(date_1.valid_date('01-02-2022'))
