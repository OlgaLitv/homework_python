"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
«Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках
реализуйте параметры, уникальные для каждого типа оргтехники."""

import datetime


class Warehouse:
    def __init__(self, name):
        self.__name = name
        self.__equipment = []


class OfficeEquipment:
    def __init__(self, maker, model, production_date, serial_number, item_number, speed, ciss='No', year_of_receipt=None):
        """ maker - производитель, model - модель, ciss - система непрырывной подачи чернил,
        item_number - инвентаризационный номер, year_of_receipt - год поступления на склад,
        production_date - год производства, serial_number - серийный номер """
        self._maker, self._model = maker, model
        self._item_number, self._serial_number = item_number, serial_number
        self._production_date = production_date
        self._CISS, self._speed = ciss, speed
        self._year = year_of_receipt if year_of_receipt else datetime.datetime.now()

    def __str__(self):
        info = 'Information about ' + self.__class__.__name__ + '\n'
        print(self.__dict__.__str__())
        for key, item in self.__dict__.items():
            info += f'{key[1:]:15s} = {item}\n'
        return info


class Printer(OfficeEquipment):
    def __init__(self, maker, model, production_date, serial_number, item_number, type_pr, cartridge, speed,
                 year_of_receipt=None, ciss='No'):
        self._type = type_pr
        self._cartridge = cartridge
        super().__init__(maker, model, production_date, serial_number, item_number, speed, ciss, year_of_receipt)


class Scaner(OfficeEquipment):
    pass


class MFU(OfficeEquipment):
    def __init__(self, maker, model, production_date, cartridge, speed, type_pr, serial_number,
                 item_number, ciss='No', year_of_receipt=None):
        self._cartridge = cartridge
        self._type = type_pr
        super().__init__(maker, model, production_date, serial_number, item_number, speed, ciss, year_of_receipt)


class Shredder(OfficeEquipment):
    pass


pr = Printer(maker='HP', model='Laser 107a 4ZB77A', production_date=2018, type_pr='laser', item_number='000010',
             serial_number='193015506374', speed='20 стр/мин', cartridge='Картридж HP 106A (W1106A)',
             year_of_receipt=2019)
print(pr)

mfu = MFU(maker='Epson', model='L7180 C11CG16404', production_date=2019, type_pr='inkjet', item_number='000012',
             serial_number='585241058156', speed='28 стр/мин', cartridge='Картридж',
             year_of_receipt=2019, ciss='Yes')
print(mfu)
scan = Scaner(maker='Brother', model='L7', production_date=2019, item_number='000023',
             serial_number='585241058156', speed='10 стр/мин',
             year_of_receipt=2019)
print(scan)
