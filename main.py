import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.move_cars()
    if player.finish():
        car.increase_speed()
        scoreboard.update_level()
    for c in car.cars:
        if player.distance(c) < 15:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
