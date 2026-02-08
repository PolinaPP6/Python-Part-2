# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Material:
    """
    Документация на класс.
    Класс описывает материал.
    """
    def __init__(self, name: str, density: float, module_of_elasticity: float):
        """
        Инициализация класса
        :param name: Название материала
        :param density: Плотность материала
        :param module_of_elasticity: Модуль упругости материала
        """
        self.name = name
        self.density = density
        self.module_of_elasticity = module_of_elasticity

        if not isinstance(density, (int, float)):
            raise TypeError("Плотность материала должна быть типа int или float")
        if density <= 0:
            raise ValueError("Плотность материала должна быть положительным числом")
        self.density = density

        if not isinstance(module_of_elasticity, (int, float)):
            raise TypeError("Модуль упругости должен быть int или float")
        if module_of_elasticity < 0:
            raise ValueError("Модуль упругости не может быть отрицательным числом")
        self.module_of_elasticity = module_of_elasticity

    def weight(self, volume: float) -> None:
        """
        Вычисление массы материала
        :param volume: Объем материала

        :raise ValueError: Если объем будет не типа int или float вызывается ошибка;
                            Если объем будет отрицательным, то вызывается ошибка
        """
        ...

    def tension(self, relative_elongation: float) -> None:
        """
        Вычисление напряжения материала
        :param relative_elongation: относительное удлинение

        :raise ValueError: Если относительное удлинение будет не типа int или float вызывается ошибка;

        """
        ...


class Bus:
    """
    Документация на класс.
    Класс описывает параметры автобуса.
    """

    def __init__(self, number: int, number_of_seats: int):
        """
        Инициализация класса
        :param number: Номер автобуса
        :param number_of_seats: Количество мест в автобусе
        """
        self.number = number
        self.number_of_seats = number_of_seats

        if not isinstance(number, (int, float)):
            raise TypeError("Номер автобуса должен быть типа int или float")
        if number <= 0:
            raise ValueError("Номер автобуса должен быть положительным числом")
        self.number = number

        if not isinstance(number_of_seats, (int, float)):
            raise TypeError("Количество мест в автобусе должно быть типа int или float")
        if number_of_seats < 0:
            raise ValueError("Количество мест в автобусе не может быть отрицательным числом")
        self.number_of_seats = number_of_seats

    def is_empty_bus(self) -> bool:
        """
        Функция проверяет является ли автобус пустым

        :return: Является ли автобус пустым
        """
        ...

    def add_passenger_to_bus(self, passenger: int) -> None:
        """
        Вычисление напряжения материала
        :param passenger: Добавляемые пассажиры

        :raise ValueError: Если количество добавляемых пассажиров больше, чем мест в автобусе вызывается ошибка;
                            Если количество добавляемых пассажиров будет не типа int или float вызывается ошибка;
                            Если количество добавляемых пассажиров будет отрицательным, то вызывается ошибка;
        """
        ...


class Phone:
    """
    Документация на класс.
    Класс описывает мобильный телефон.
    """

    def __init__(self, memory: int, number_of_sim_cards: int):
        """
        Инициализация класса
        :param memory: Память телефона
        :param number_of_sim_cards: Количество сим карт
        """
        self.memory = memory
        self.number_of_SIM_cards = number_of_sim_cards

        if not isinstance(memory, (int, float)):
            raise TypeError("Память должна быть типа int или float")
        if memory <= 0:
            raise ValueError("Память должна быть положительным числом")
        self.memory = memory

        if not isinstance(number_of_sim_cards, (int, float)):
            raise TypeError("Количество сим карт должно быть типа int или float")
        if number_of_sim_cards < 0:
            raise ValueError("Количество сим карт не может быть отрицательным числом")
        self.number_of_SIM_cards = number_of_sim_cards

    def download_file(self, file: float) -> None:
        """
        Функция загрузки файла на мобильный телефон (добавление файла на телефон)
        :param file: Объем файла

        :raise ValueError: Если объем файла будет не типа int или float вызывается ошибка;
                            Если объем файла будет отрицательным, то вызывается ошибка;
                            Если объем файла будет больше чем объем памяти на телефоне, то вызывается ошибка
        """
        ...

    def add_sim_card(self, new_card: float) -> None:
        """
        Добавление сим карты в мобильный телефон
        :param new_card: количество добавляемых сим карт

        :raise ValueError: Если количество сим карт будет не типа int или float вызывается ошибка;
                            Если количество сим карт будет отрицательным, то вызывается ошибка;
                            Если количество сим карт будет больше чем возможно добавить в телефон, то вызывается ошибка
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    # pass
