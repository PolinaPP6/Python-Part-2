if __name__ == "__main__":
    from abc import ABC, abstractmethod
    from typing import Optional, Union
    class MusicalInstrument(ABC):
        """
        Базовый абстрактный класс для всех музыкальных инструментов.

        Определяет общие свойства и поведение для всех музыкальных инструментов.
        """

        def __init__(self, name: str, brand: str, price: float):
            """
            Инициализация музыкального инструмента.

            Args:
                name: Название инструмента
                brand: Производитель
                price: Цена в рублях
            """
            self._name = name  # Название инструмента
            self._brand = brand  # Бренд
            self._price = price  # Цена
            self._is_tuned: bool = True  # Состояние настройки

        def play(self) -> str:
            """
            Базовый метод воспроизведения звука.

            Returns:
                Строка с описанием воспроизводимого звука
            """
            if not self._is_tuned:
                return f"{self._name} расстроен и звучит фальшиво!"
            return f"{self._name} издает звук"

        def tune(self) -> str:
            """
            Настройка инструмента.

            Returns:
                Строка с результатом настройки
            """
            self._is_tuned = True
            return f"{self._name} настроен"

        def __str__(self) -> str:
            """
            Пользовательское строковое представление инструмента.

            Returns:
                Описание инструмента для пользователей
            """
            return f"{self._brand} {self._name} - {self._price} руб."

        def __repr__(self) -> str:
            """
            Официальное строковое представление инструмента для разработчиков.

            Returns:
                Строка, которую можно использовать для воссоздания объекта
            """
            return f"{self.__class__.__name__}(name='{self._name}', brand='{self._brand}', price={self._price})"

        @abstractmethod
        def get_instrument_type(self) -> str:
            """Абстрактный метод для получения типа инструмента."""
            pass


    class Guitar(MusicalInstrument):
        """
        Класс гитары, наследующийся от MusicalInstrument.
        """

        def __init__(self, name: str, brand: str, price: float, strings_count: int = 6):
            """
            Расширенный конструктор класса Guitar.

            Args:
                name: Название гитары
                brand: Производитель
                price: Цена
                strings_count: Количество струн (по умолчанию 6)
            """
            super().__init__(name, brand, price)
            self._strings_count = strings_count  # Количество струн

        def play(self) -> str:
            """
            Перегруженный метод воспроизведения.

            Причина перегрузки: Гитара имеет специфический звук, который зависит
            от количества струн и способа игры.

            Returns:
                Строка с описанием игры на гитаре
            """
            base_sound = super().play()
            if not self._is_tuned:
                return base_sound

            if self._strings_count == 12:
                return f"{base_sound}: играем аккорды на 12-струнной гитаре с богатым звучанием"
            return f"{base_sound}: играем аккорды на {self._strings_count}-струнной гитаре"

        def tune(self) -> str:
            """
            Перегруженный метод настройки для гитары.

            Причина перегрузки: Гитара требует настройки каждой струны отдельно.

            Returns:
                Строка с результатом настройки гитары
            """
            result = super().tune()
            return f"{result} и настроены все {self._strings_count} струн"

        def get_instrument_type(self) -> str:
            """Реализация абстрактного метода."""
            return "Струнный щипковый инструмент"


    class Piano(MusicalInstrument):
        """
        Класс пианино, наследующийся от MusicalInstrument.
        """

        def __init__(self, name: str, brand: str, price: float, key_count: int = 88):
            """
            Расширенный конструктор класса Piano.

            Args:
                name: Название пианино
                brand: Производитель
                price: Цена
                key_count: Количество клавиш (по умолчанию 88)
            """
            super().__init__(name, brand, price)
            self._key_count = key_count  # Количество клавиш
            self._is_electronic: bool = False  # Тип пианино

        def play(self) -> str:
            """
            Перегруженный метод воспроизведения.

            Причина перегрузки: Пианино имеет клавишный механизм и может играть
            одновременно несколько нот (аккорды).

            Returns:
                Строка с описанием игры на пианино
            """
            base_sound = super().play()
            if not self._is_tuned:
                return base_sound

            instrument_type = "электронное" if self._is_electronic else "акустическое"
            return f"{base_sound}: нажимаем клавиши на {instrument_type} пианино с {self._key_count} клавишами"

        def tune(self) -> str:
            """
            Перегруженный метод настройки для пианино.

            Причина перегрузки: Настройка пианино требует специального оборудования
            и занимает много времени.

            Returns:
                Строка с результатом настройки пианино
            """
            if self._is_electronic:
                return f"{self._name} - электронное пианино, не требует настройки"

            result = super().tune()
            return f"{result} (требуется вызов настройщика для {self._key_count} клавиш)"

        def get_instrument_type(self) -> str:
            """Реализация абстрактного метода."""
            return "Клавишный инструмент"

        def set_electronic(self, is_electronic: bool) -> None:
            """
            Установка типа пианино (электронное или акустическое).

            Args:
                is_electronic: True для электронного, False для акустического
            """
            self._is_electronic = is_electronic

    pass
