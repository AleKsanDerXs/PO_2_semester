"""
Скрипт для создания анимированной иллюзии с использованием turtle.
"""
import turtle
import time
import argparse

def draw_animated_illusion(num_spokes, colors, radius, extent, rotation_angle, delay):
    """
    Рисует анимированную иллюзию с использованием turtle.
    
    Args:
        num_spokes (int): Количество лучей.
        colors (list): Список цветов для чередования.
        radius (int): Радиус дуги.
        extent (int): Угол дуги в градусах (0 для прямой линии).
        rotation_angle (int): Угол поворота для анимации.
        delay (float): Задержка в секундах между кадрами.
    """
    turtle.speed(0)
    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.tracer(0)
    turtle.pensize(2)

    angle = 360 / num_spokes

    while True:
        turtle.clear()
        for i in range(num_spokes):
            turtle.pencolor(colors[i % len(colors)])
            turtle.penup()
            turtle.goto(0, 0)
            turtle.pendown()
            turtle.setheading(i * angle + turtle.heading())
            if extent == 0:
                turtle.forward(radius)
            else:
                turtle.circle(radius, extent)
        turtle.update()
        time.sleep(delay)
        turtle.right(rotation_angle)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Создание анимированной иллюзии")
    parser.add_argument("--num_spokes", type=int, required=True, help="Количество лучей")
    parser.add_argument("--colors", type=str, required=True, help="Цвета через запятую")
    parser.add_argument("--radius", type=int, required=True, help="Радиус дуги")
    parser.add_argument("--extent", type=int, required=True, help="Угол дуги")
    parser.add_argument("--rotation_angle", type=int, required=True, help="Угол поворота")
    parser.add_argument("--delay", type=float, required=True, help="Задержка в секундах")
    args = parser.parse_args()

    colors = [color.strip() for color in args.colors.split(",")]
    draw_animated_illusion(args.num_spokes, colors, args.radius, args.extent, args.rotation_angle, args.delay)