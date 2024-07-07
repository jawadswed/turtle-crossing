import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_cars()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        for i in range(20):
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            rand_color = random.randint(0, len(COLORS) - 1)
            car_color = COLORS[rand_color]
            new_car.color(car_color)
            new_car.penup()
            rand_x = random.randint(-280, 280)
            rand_y = random.randint(-250, 270)
            new_car.goto(rand_x, rand_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.setheading(180)
            car.fd(self.car_speed)
            if car.xcor() < -280:
                car.goto(280, car.ycor())

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

