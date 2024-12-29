# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 17:49:36 2024

@author: YASEMİN
"""

import turtle
import time
import random

# Ekran ayarları
win = turtle.Screen()
win.title("Yılan Oyunu")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)  # Ekranda güncellemeleri kapat

# Yılan başlangıç konumu ve boyutu
snake = turtle.Turtle()
snake.speed(0)
snake.shape("circle")
snake.color("yellow")
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"

# Yılanın vücudu
snake_segments = []

# Yem konumu ve boyutu
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("pink")
food.penup()
food.goto(0, 100)

# Yılanın hareketi
def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

# Tuş bağlama
win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")
win.onkey(go_right, "Right")

# Yılanın hareketi fonksiyonu
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Yılanın vücudunu başlangıç pozisyonuna döndür
def reset_snake():
    snake.goto(0, 0)
    snake.direction = "Stop"

    for segment in snake_segments:
        segment.goto(1000, 1000)  # Ekran dışına taşı

    snake_segments.clear()

# Oyun döngüsü
while True:
    win.update()

    # Yılanın sınırları kontrolü
    if (
        snake.xcor() > 290 or snake.xcor() < -290 or
        snake.ycor() > 290 or snake.ycor() < -290
    ):
        print("Game Over")
        time.sleep(1)
        reset_snake()

    # Yılanın yemi yemesi
    if snake.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Yılanı uzat
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("yellow")
        new_segment.penup()
        snake_segments.append(new_segment)

    # Yılanın vücudunu güncelle
    for i in range(len(snake_segments) - 1, 0, -1):
        x = snake_segments[i - 1].xcor()
        y = snake_segments[i - 1].ycor()
        snake_segments[i].goto(x, y)

    if len(snake_segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        snake_segments[0].goto(x, y)

    move()

    time.sleep(0.1)
    
