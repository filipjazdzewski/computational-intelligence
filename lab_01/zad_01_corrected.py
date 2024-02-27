import math
from datetime import date


def get_user_input():
    name = input("Podaj swoje imię: ")
    year_of_birth = int(input("Podaj rok urodzenia: "))
    month_of_birth = int(input("Podaj miesiąc urodzenia: "))
    day_of_birth = int(input("Podaj dzień urodzenia: "))
    return name, year_of_birth, month_of_birth, day_of_birth


def calculate_days_old(year_of_birth, month_of_birth, day_of_birth):
    today = date.today()
    date_of_birth = date(year_of_birth, month_of_birth, day_of_birth)
    return (today - date_of_birth).days


def calculate_wave(days_old, period):
    return math.sin(math.pi * 2 * days_old / period)


def print_wave_info(wave_type, wave_value):
    print(f"Twoja fala {wave_type} wynosi: {wave_value}")


def main():
    name, year_of_birth, month_of_birth, day_of_birth = get_user_input()
    days_old = calculate_days_old(year_of_birth, month_of_birth, day_of_birth)

    print(f"Cześć {name}! Jesteś na świecie już {days_old} dni.")

    # a)
    physical_wave = calculate_wave(days_old, 23)
    emotional_wave = calculate_wave(days_old, 28)
    intelectual_wave = calculate_wave(days_old, 33)

    print_wave_info("fizyczna", physical_wave)
    print_wave_info("emocjonalna", emotional_wave)
    print_wave_info("intelektualna", intelectual_wave)

    # b)
    physical_wave_tomorrow = calculate_wave(days_old + 1, 23)
    emotional_wave_tomorrow = calculate_wave(days_old + 1, 28)
    intelectual_wave_tomorrow = calculate_wave(days_old + 1, 33)

    if physical_wave > 0.5:
        print("Dzisiaj jest dobry dzień na ćwiczenia fizyczne.")
    elif physical_wave < -0.5:
        print("Dzisiaj jest dobry dzień na odpoczynek fizyczny.")
        if physical_wave_tomorrow > physical_wave:
            print("Nie martw się. Jutro będzie lepiej!")
    else:
        print("Dzisiaj jest okej dzień fizycznie. Ani za bardzo, ani za mało.")

    if emotional_wave > 0.5:
        print("Dzisiaj jest dobry dzień na spotkanie z przyjaciółmi.")
    elif emotional_wave < -0.5:
        print("Dzisiaj jest dobry dzień na odpoczynek emocjonalny.")
        if emotional_wave_tomorrow > emotional_wave:
            print("Nie martw się. Jutro będzie lepiej!")
    else:
        print("Dzisiaj jest okej dzień emocjonalnie. Ani za bardzo, ani za mało.")

    if intelectual_wave > 0.5:
        print("Dzisiaj jest dobry dzień na naukę.")
    elif intelectual_wave < -0.5:
        print("Dzisiaj jest dobry dzień na odpoczynek intelektualny.")
        if intelectual_wave_tomorrow > intelectual_wave:
            print("Nie martw się. Jutro będzie lepiej!")
    else:
        print("Dzisiaj jest okej dzień intelektualnie. Ani za bardzo, ani za mało.")


if __name__ == "__main__":
    main()
