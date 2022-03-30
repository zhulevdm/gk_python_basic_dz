from my_exception import CheckValue
from abc import ABC, abstractmethod


class Warehouse:
    def __init__(self):
        self._count_equipment = {'Принтер' : 0, 'Сканер' : 0,'Копир' : 0,}
        self._equipment = []
    
    def receive(self, unit, number):
        try:
            if not isinstance(number, int):
                raise CheckValue(f'Не удалось добавить на склад {unit}. Значение кол-ва должно быть число!')
            self._count_equipment[unit.device] += number
            for i in range(number):
                self._equipment.append(unit)
                unit.parent = self
        except CheckValue as err:
            print(err)
        
    def remove(self, unit, number):
        self._count_equipment[unit.device] -= number
        for i in range(number):
            self._equipment.remove(unit)
            unit.parent = None


class OfficeEquipment(ABC):
    def __init__(self, device, vendor, paper_size):
        self.paper_size = paper_size
        self.vendor = vendor
        self.device = device
        self.some_value = None
    
    def __str__(self):
        return f'{self.device}: {self.vendor}, {self.paper_size}, {self.some_value}'
        
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, unit):
        self._parent = unit
        
        
class Printer(OfficeEquipment):
    def __init__(self, device, vendor, paper_size, duplex='no duplex'):
        super().__init__(device, vendor, paper_size)
        self.some_value = duplex


class Scanner(OfficeEquipment):
    def __init__(self, device, vendor, paper_size, autofeed='no autofeed'):
        super().__init__(device, vendor, paper_size)
        self.some_value = autofeed


class Copier(OfficeEquipment):
    def __init__(self, device, vendor, paper_size, color='grayscale'):
        super().__init__(device, vendor, paper_size)
        self.some_value = color
