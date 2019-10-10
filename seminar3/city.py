import math

#Chromossomes

class City:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name

    def print(self):
        print(self.name + " located at x: " + str(self.x) + " / y: " + str(self.y) + "\n")

    def distance(self, another_city):
        return math.sqrt( math.pow((another_city.x - self.x),2)  + math.pow((another_city.y - self.y) , 2))

    def __eq__(self, city):
        return self.x == city.x and self.y == city.y and self.name == city.name