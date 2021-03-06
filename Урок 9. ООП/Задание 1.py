# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
import time
from time import sleep


class TrafficLight:
    __color = 'red'

    def running(self):
        print(TrafficLight.__color)
        time.sleep(7)
        TrafficLight.__color = 'yellow'
        print(TrafficLight.__color)
        time.sleep(2)
        TrafficLight.__color = 'green'
        print(TrafficLight.__color)
        time.sleep(3)


traffic_light_1 = TrafficLight()
traffic_light_1.running()
