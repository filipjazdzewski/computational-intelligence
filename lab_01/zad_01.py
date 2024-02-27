import math
from datetime import date

# Czas wykonania zadania: 20 minut

name = input("Podaj swoje imię: ")
year_of_birth = int(input("Podaj rok urodzenia: "))
month_of_birth = int(input("Podaj miesiąc urodzenia: "))
day_of_birth = int(input("Podaj dzień urodzenia: "))

today = date.today()
date_of_birth = date(year_of_birth, month_of_birth, day_of_birth)
days_old = (today - date_of_birth).days

print(f"Cześć {name}! Jesteś na świecie już {days_old} dni.")

# a)
TWO_PI_DAYS_OLD = math.pi * 2 * days_old
physical_wave = math.sin(TWO_PI_DAYS_OLD / 23)
emotional_wave = math.sin(TWO_PI_DAYS_OLD / 28)
intelectual_wave = math.sin(TWO_PI_DAYS_OLD / 33)

print(f"Twoja fala fizyczna wynosi: {physical_wave}")
print(f"Twoja fala emocjonalna wynosi: {emotional_wave}")
print(f"Twoja fala intelektualna wynosi: {intelectual_wave}")

# b)
TWO_PY_DAYS_OLD_TOMMOROW = math.pi * 2 * (days_old + 1)
physical_wave_tommorow = math.sin(TWO_PY_DAYS_OLD_TOMMOROW / 23)
emotional_wave_tommorow = math.sin(TWO_PY_DAYS_OLD_TOMMOROW / 28)
intelectual_wave_tommorow = math.sin(TWO_PY_DAYS_OLD_TOMMOROW / 33)

if physical_wave > 0.5:
    print("Dzisiaj jest dobry dzień na ćwiczenia fizyczne.")
elif physical_wave < -0.5:
    print("Dzisiaj jest dobry dzień na odpoczynek fizyczny.")
    if physical_wave_tommorow > physical_wave:
        print("Nie martw się. Jutro będzie lepiej!")
else:
    print("Dzisiaj jest okej dzień fizycznie. Ani za bardzo, ani za mało.")

if emotional_wave > 0.5:
    print("Dzisiaj jest dobry dzień na spotkanie z przyjaciółmi.")
elif emotional_wave < -0.5:
    print("Dzisiaj jest dobry dzień na odpoczynek emocjonalny.")
    if emotional_wave_tommorow > emotional_wave:
        print("Nie martw się. Jutro będzie lepiej!")
else:
    print("Dzisiaj jest okej dzień emocjonalnie. Ani za bardzo, ani za mało.")

if intelectual_wave > 0.5:
    print("Dzisiaj jest dobry dzień na naukę.")
elif intelectual_wave < -0.5:
    print("Dzisiaj jest dobry dzień na odpoczynek intelektualny.")
    if intelectual_wave_tommorow > intelectual_wave:
        print("Nie martw się. Jutro będzie lepiej!")
else:
    print("Dzisiaj jest okej dzień intelektualnie. Ani za bardzo, ani za mało.")
