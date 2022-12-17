# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

quater = input()

match quater:
    case "1":
        print("x > 0, y > 0")
    case "2":
        print("x < 0, y > 0")
    case "3":
        print("x < 0, y < 0")
    case "4":
        print("x > 0, y < 0")
    case _:
        print("error")