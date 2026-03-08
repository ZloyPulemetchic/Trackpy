from typing import Optional


class Vehicle:
    """
    Базовый класс для представления транспортного средства.

    Attributes:
        brand (str): Производитель транспортного средства.
        model (str): Модель транспортного средства.
        year (int): Год выпуска.
        _mileage (float): Пробег автомобиля. Сделан непубличным для предотвращения
        прямого изменения пользователем.
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float = 0) -> None:
        """
        Конструктор базового класса Vehicle.

        Args:
            brand (str): Производитель.
            model (str): Модель.
            year (int): Год выпуска.
            mileage (float): Пробег автомобиля.
        """
        self.brand: str = brand
        self.model: str = model
        self.year: int = year
        self._mileage: float = mileage  # инкапсуляция

    def __str__(self) -> str:
        """
        Возвращает удобочитаемое строковое представление объекта.
        """
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает строку, пригодную для отладки и воссоздания объекта.
        """
        return f"Vehicle(brand='{self.brand}', model='{self.model}', year={self.year}, mileage={self._mileage})"

    def drive(self, distance: float) -> None:
        """
        Увеличивает пробег автомобиля.

        Args:
            distance (float): расстояние поездки в километрах.
        """
        if distance > 0:
            self._mileage += distance

    def get_mileage(self) -> float:
        """
        Возвращает текущий пробег автомобиля.

        Returns:
            float: пробег.
        """
        return self._mileage


class ElectricCar(Vehicle):
    """
    Класс электромобиля, наследующий базовый класс Vehicle.

    Attributes:
        battery_capacity (float): Ёмкость батареи (кВт⋅ч).
        charge_level (float): Текущий уровень заряда батареи (0–100%).
    """

    def __init__(
            self,
            brand: str,
            model: str,
            year: int,
            battery_capacity: float,
            charge_level: float = 100,
            mileage: float = 0
    ) -> None:
        """
        Конструктор электромобиля.

        Расширяет конструктор базового класса Vehicle,
        добавляя характеристики батареи.

        Args:
            brand (str): Производитель.
            model (str): Модель.
            year (int): Год выпуска.
            battery_capacity (float): Ёмкость батареи.
            charge_level (float): Уровень заряда.
            mileage (float): Пробег.
        """
        super().__init__(brand, model, year, mileage)

        self.battery_capacity: float = battery_capacity
        self.charge_level: float = charge_level

    def __str__(self) -> str:
        """
        Переопределённое строковое представление электромобиля.
        """
        return f"{self.brand} {self.model} ({self.year}) - Electric, charge: {self.charge_level}%"

    def __repr__(self) -> str:
        """
        Представление объекта для разработчиков.
        """
        return (
            f"ElectricCar(brand='{self.brand}', model='{self.model}', year={self.year}, "
            f"battery_capacity={self.battery_capacity}, charge_level={self.charge_level})"
        )

    def drive(self, distance: float) -> None:
        """
        Перегруженная версия метода drive.

        Причина перегрузки:
        У электромобилей во время движения расходуется заряд батареи,
        поэтому необходимо дополнительно уменьшать уровень заряда.

        Args:
            distance (float): расстояние поездки.
        """
        super().drive(distance)

        consumption_rate: float = 0.2  # условный расход % заряда на км
        self.charge_level -= distance * consumption_rate

        if self.charge_level < 0:
            self.charge_level = 0

    def charge(self) -> None:
        """
        Полностью заряжает батарею автомобиля.
        """
        self.charge_level = 100