"""3. Реализовать базовый класс Employee (сотрудник).
определить атрибуты: name (имя), surname (фамилия), которые должны передаваться при создании экземпляра Employee;
создать класс Position (должность) с аттрибутами employee (сотрудник/Employee), position (должность/str),
income (вознаграждение/dict) - атрибуты также задаются при создании экземпляра класса;
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus};
в классе Position реализовать методы получения полного имени сотрудника get_full_name() и дохода с учётом премии
get_total_income() (wage + bonus);
проверить работу примера на реальных данных: создать экземпляры классов Employee, Position, вывести на экран имя
сотрудника, его должность и вознаграждение сотрудника, используя методы класса Position."""


class Employee:

    def __init__(self, name, surname):
        self._name, self._surname = name, surname

    def get_full_name(self):
        return self._name + ' ' + self._surname


class Position:

    def __init__(self, empl, position, wage, bonus):
        if isinstance(empl, Employee):
            self._employee = empl
        else:
            raise ValueError('Give employee, please')
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

    def get_full_name(self):
        return self._employee.get_full_name()

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


empl1, empl2 = Employee('Олег', 'Титов'), Employee('Петр', 'Китов')
pos1 = Position(empl1, 'менеджер по продажам', wage=50000, bonus=20000)
pos2 = Position(empl2, 'аналитик', wage=60000, bonus=30000)
pos3 = Position(Employee('Марина', 'Маслова'), 'начальник отдела кадров', wage=70000, bonus=40000)
pos4 = Position(Employee('Анна', 'Ковалева'), 'генеральный директор', wage=90000, bonus=40000)
print(pos1.get_full_name(), ',', pos1.position, pos1.get_total_income())
print(pos2.get_full_name(), ',', pos2.position, pos2.get_total_income())
print(pos3.get_full_name(), ',', pos3.position, pos3.get_total_income())
print(pos4.get_full_name(), ',', pos4.position, pos4.get_total_income())
