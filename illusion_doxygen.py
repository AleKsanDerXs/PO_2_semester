"""
\\file illusion.py
\\brief Скрипт для создания анимированной иллюзии с использованием turtle.

\\mainpage Документация к проекту Illusion

Этот скрипт позволяет пользователю ввести параметры для создания анимированной иллюзии,
такие как количество лучей, цвета, радиус, угол дуги, угол поворота и задержку, а в конце увидеть результат
в виде анимации.

\\section intro Введение
Целью проекта является демонстрация возможностей библиотеки turtle для создания интерактивных и визуально привлекательных анимаций.

\\section usage Использование
Для запуска скрипта выполните команду:
\\code
python illusion.py
\\endcode
Затем следуйте инструкциям в консоли для ввода параметров.

\\section params Параметры
- num_spokes: Количество лучей (палок).
- colors: Список цветов для чередования между лучами.
- radius: Радиус дуги.
- extent: Угол дуги в градусах (0 для прямой линии).
- rotation_angle: Угол поворота для анимации в градусах.
- delay: Задержка в секундах между кадрами анимации.
"""

import turtle
import time

def draw_animated_illusion(num_spokes, colors, radius, extent, rotation_angle, delay):
    """
    \\brief Рисует анимированную иллюзию с использованием turtle.

    Эта функция создает анимированную иллюзию, рисуя "палки" (дуги) в виде лучей, 
    исходящих из центра, с возможностью настройки количества лучей, цветов, радиуса, 
    угла дуги, угла поворота и задержки анимации.

    \\param num_spokes Количество лучей (палок).
    \\param colors Список цветов для чередования между лучами.
    \\param radius Радиус дуги.
    \\param extent Угол дуги в градусах (0 для прямой линии).
    \\param rotation_angle Угол поворота для анимации в градусах.
    \\param delay Задержка в секундах между кадрами анимации.
    """
    # Настраиваем turtle
    turtle.speed(0)  # Максимальная скорость рисования
    turtle.bgcolor("black")  # Черный фон для контраста
    turtle.hideturtle()  # Скрываем стрелку
    turtle.tracer(0)  # Отключаем автоматическое обновление для плавности
    turtle.pensize(2)

    angle = 360 / num_spokes  # Угол между "палками"

    while True:  # Бесконечный цикл для анимации
        turtle.clear()  # Очищаем экран перед новым кадром
        for i in range(num_spokes):
            # Чередуем цвета из списка
            turtle.pencolor(colors[i % len(colors)])
            turtle.penup()  # Поднимаем перо, чтобы вернуться в центр
            turtle.goto(0, 0)  # Центр
            turtle.pendown()  # Опускаем перо для рисования
            turtle.setheading(i * angle + turtle.heading())  # Устанавливаем угол
            # Рисуем дугу вместо прямой линии
            if (extent == 0):
                turtle.forward(radius)
            else:
                turtle.circle(radius, extent)
        turtle.update()  # Обновляем экран
        time.sleep(delay)  # Задержка для плавной анимации
        turtle.right(rotation_angle)  # Поворачиваем весь узор

# Получаем ввод от пользователя
num_spokes = int(input("Введите количество палок: "))
colors_input = input("Введите цвета через запятую (например, red,blue,yellow): ")
colors = [color.strip() for color in colors_input.split(",")]  # Разбиваем на список
radius = int(input("Введите радиус дуги: "))
extent = int(input("Введите угол дуги (например, 60 для 60 градусов): "))
rotation_angle = int(input("Введите угол поворота для анимации (например, 5): "))
delay = float(input("Введите задержку в секундах (например, 0.1): "))

# Запускаем иллюзию
draw_animated_illusion(num_spokes, colors, radius, extent, rotation_angle, delay)