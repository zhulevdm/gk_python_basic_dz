from my_compo import Warehouse, Printer, Scanner, Copier


warehouse = Warehouse()
scanner = Scanner('Сканер', 'HP', 'A4')
printer = Printer('Принтер', 'HP', 'A4')
copier = Copier('Копир', 'Xerox', 'A4', 'color')

print(scanner)
print(printer)
print(copier)

warehouse.receive(printer, 4)
warehouse.receive(scanner, 4)
warehouse.receive(copier, '3')
warehouse.receive(copier, 3)

print(warehouse._count_equipment)

warehouse.remove(scanner, 2)

print(warehouse._count_equipment)
