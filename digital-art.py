import turtle
import random

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(255)  # <-- разрешаем задавать цвета в диапазоне 0-255

# Создаём черепашку
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)  # немного толщины для красоты

# Рисуем узор из кругов
for i in range(50):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pen.pencolor((r, g, b))  # <-- передаём кортеж

    pen.circle(i * 10, random.randint(100, 200))
    pen.rt(30)

screen.exitonclick()