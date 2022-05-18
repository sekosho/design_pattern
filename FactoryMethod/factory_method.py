from abc import ABC, abstractmethod, abstractproperty


class IFactory(ABC):
    def __init__(self) -> None:
        self.registered_owners = []

    def create(self, owner):
        self._owner = owner
        product = self._create_product()
        self._register_product(product)
        return product

    @abstractmethod
    def _create_product(self):
        pass

    @abstractmethod
    def _register_product(self, product):
        pass


class CarFactory(IFactory):
    def _create_product(self):
        return Car(self._owner)

    def _register_product(self, product):
        self.registered_owners.append(product.owner)


class ShipFactory(IFactory):
    def _create_product(self):
        return Ship(self._owner)

    def _register_product(self, product):
        self.registered_owners.append(product.owner)


class IProduct(ABC):
    def __init__(self, owner) -> None:
        self._owner = owner

    @abstractmethod
    def use(self):
        pass

    @abstractproperty
    def owner(self):
        pass


class Car(IProduct):
    @property
    def owner(self):
        return self._owner

    def use(self):
        print(f"{self.owner}は車を運転します")


class Ship(IProduct):
    @property
    def owner(self):
        return self._owner

    def use(self):
        print(f"{self.owner}は船を運転します")


car_factory = CarFactory()
sesoko_car = car_factory.create("瀬底")
takagi_car = car_factory.create("高木")
sesoko_car.use()
takagi_car.use()
print(car_factory.registered_owners)


ship_factory = ShipFactory()
mike_ship = ship_factory.create("Mike")
john_ship = ship_factory.create("John")
mike_ship.use()
john_ship.use()
print(ship_factory.registered_owners)
