import math
import random
import matplotlib.pyplot as plt
import numpy as np

"""
--- Notatka ---
Gdy pytałem chatGPT o to, jak zrobić takie zadanie, miał on problem z
napisaniem wzoru z uwzględnieniem wysokości początkowej. Musiałem go często 
poprawiać. Jeżeli chodzi o zmiany w kodzie to chat zazwyczaj w swoim kodzie 
dodawał funkcję main, która wywoływała wszystkie funkcje. W moim przypadku nie 
było to potrzebne, ponieważ kod jest krótki i czytelny.
"""

HEIGHT = 100
VELOCITY = 50
MARGIN = 5
EARTH_G = 9.81


def calc_projectile_range(angle, v, h, g):
    angle_rad = math.radians(angle)
    range_distance = (v * math.cos(angle_rad) / g) * (
        v * math.sin(angle_rad) + math.sqrt((v * math.sin(angle_rad)) ** 2 + 2 * g * h)
    )

    return round(range_distance, 2)


def is_target_hit(projectile_range, target_distance, margin):
    return abs(projectile_range - target_distance) <= margin


def plot_projectile_trajectory(projectile_range, angle, v, h, g):
    # dzieli oś x na 100 równych części
    x = np.linspace(0, projectile_range, 100)
    # wzór na trajektorię rzutu ukośnego
    y = (
        h
        + x * math.tan(math.radians(angle))
        - (g * x**2) / (2 * v**2 * math.cos(math.radians(angle)) ** 2)
    )
    plt.plot(x, y, color="blue")
    plt.grid(True)
    plt.xlabel("Odległość [m]")
    plt.ylabel("Wysokość [m]")
    plt.title("Trajektoria lotu pocisku trebusza")
    plt.savefig("trajektoria.png")
    plt.show()


target_distance_random = random.randint(50, 340)
print("Odległość od celu: ", target_distance_random, "m")

attempts = 0
while True:
    attempts += 1
    angle = float(input("Podaj kąt: "))

    projectile_range = calc_projectile_range(angle, VELOCITY, HEIGHT, EARTH_G)

    if is_target_hit(projectile_range, target_distance_random, MARGIN):
        print("Cel trafiony! Liczba prób: ", attempts)

        plot_projectile_trajectory(projectile_range, angle, VELOCITY, HEIGHT, EARTH_G)
        break
    else:
        print("Zasięg strzału: ", projectile_range, "m")
