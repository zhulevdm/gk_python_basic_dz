import time


class TrafficLight:
    
    def __init__(self):
        self.__color = {'red':4, 'yellow':2, 'green':3}

    def running(self):
        for color, duration in self.__color.items():
            print(f'{color} {duration} сек')
            time.sleep(duration)


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
