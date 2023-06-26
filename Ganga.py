import threading
import time


class MarijuanaBush:
    def __init__(self):
        self.health = 100
        self.thirst = 0
        self.fertilizer = 0
        self.temperature = 25

    def water(self):
        self.thirst -= 10
        if self.thirst < 0:
            self.thirst = 0
        self.health += 20
        if self.health > 100:
            self.health = 100

    def fertilize(self):
        self.fertilizer += 1
        self.health += 10
        if self.health > 100:
            self.health = 100

    def adjust_temperature(self, temperature):
        self.temperature = temperature

    def simulate_growth(self):
        while self.health > 0:
            self.health -= 1
            self.thirst += 1
            if self.thirst > 100:
                self.health -= 10
            if self.fertilizer > 0:
                self.health += 2
                self.fertilizer -= 1
            if self.temperature < 20 or self.temperature > 30:
                self.health -= 5

            print(
                f"Жизнь: {self.health}, Жажда: {self.thirst}, Удобрения: {self.fertilizer}, Температура: {self.temperature}")
            time.sleep(1)

        print("Ваш куст марихуаны погиб...")


# Создаем экземпляр куста марихуаны
bush = MarijuanaBush()

# Запускаем симуляцию роста куста марихуаны в отдельном потоке
growth_thread = threading.Thread(target=bush.simulate_growth)
growth_thread.start()

# Взаимодействие с пользователем
while True:
    print("Выберите действие:")
    print("1. Полить куст марихуаны")
    print("2. Удобрить куст марихуаны")
    print("3. Изменить температуру")
    print("0. Выйти")

    выбор = input("Введите номер действия: ")

    if выбор == "1":
        bush.water()
        print("Куст марихуаны полит и поблагодарил вас!")
    elif выбор == "2":
        bush.fertilize()
        print("Куст марихуаны удобрен и вырос в размере!")

2