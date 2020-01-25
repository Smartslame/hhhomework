class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return self.make + ' ' + self.model


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars):
        self.cars = cars

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, index):
        return self.cars[index]

    def add(self, car):
        self.cars.append(car)

    def delete(self, index):
        self.cars.pop(index)


if __name__ == '__main__':
    cars = [Car('bmw', 'x6'), Car('lada', '2108'), Car('lexus', 'rx 350')]
    garage = Garage(cars)
    print(len(garage))
    garage.add(Car('new', 'added'))
    garage.delete(0)
    garage.delete(len(garage) - 1)
    for car in garage:
        print(car)
