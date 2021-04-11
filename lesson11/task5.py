"""5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад
и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь)."""

import datetime
import collections


class BusinessUnit:  # склад или подразделение фирмы
    def __init__(self, name):
        self.__name = name
        self.__equipment = collections.defaultdict(int)

    @staticmethod
    def is_warehouse(self):
        return False  # True если это склад

    def take_to_the_unit(self, office_eq, num=1, get_from=None):
        """ если заполнено get_from, то это перемещение с get_from в self, если get_from не заполнено, то это
        поступление новой оргтехники извне, из магазина, например """
        if get_from:
            if get_from.__equipment[office_eq] >= num:
                get_from.__equipment[office_eq] -= num
                self.__equipment[office_eq] += num
            else:
                err = 'Этой оргтехники недостаточно: ' + office_eq.get_description() + '\n'
                err += 'Требуется: ' + str(num) + ', доступно: ' + str(get_from.__equipment[office_eq]) + '\n'
                raise ValueError(err)
        else:
            self.__equipment[office_eq] += num

    def __str__(self):
        info = self.__name + '\n'
        for key, item in self.__equipment.items():
            about = f'{key.__class__.__name__} {key._maker} {key._model}'
            info += f'{about:30s}: {item}\n'
        return info


class Warehouse(BusinessUnit):
    @staticmethod
    def is_warehouse(self):
        return True  # True если это склад


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

    def get_description(self):
        return f'{self.__class__.__name__} {self._maker} {self._model}'

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
mfu = MFU(maker='Epson', model='L7180 C11CG16404', production_date=2019, type_pr='inkjet', item_number='000012',
          serial_number='585241058156', speed='28 стр/мин', cartridge='Картридж', year_of_receipt=2019, ciss='Yes')
scan = Scaner(maker='Brother', model='L7', production_date=2019, item_number='000023',
              serial_number='466340596139', speed='10 стр/мин', year_of_receipt=2019)
sh = Shredder(maker='BRAUBERG', model='S8', production_date=2015, item_number='000031',
              serial_number='663254100993', speed='8 стр/мин', year_of_receipt=2015)
warehouse = Warehouse('Склад')
warehouse.take_to_the_unit(pr, 2)
warehouse.take_to_the_unit(sh, 1)
warehouse.take_to_the_unit(scan, 3)
warehouse.take_to_the_unit(mfu, 4)
print('до перемещения со склада')
print(warehouse)
bu1 = BusinessUnit('Подразделение 1')
bu2 = BusinessUnit('Подразделение 2')
print('после перемещения со склада в подразделение 1')
bu1.take_to_the_unit(mfu, 3, warehouse)  # перемещение со склада 3 мфу в подразделение 1
print(warehouse)
print(bu1)
print('перемещение из подразделения 2 на склад')
warehouse.take_to_the_unit(pr, 2, bu2)  # попытка переместить из подразделения 2 на склад принтер, которого там нет
print(bu2)
