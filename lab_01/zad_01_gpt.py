import datetime
import math

# Pisanie prompta: 5 minut (wynik ten sam co w zad_01.py)
"""
Could you write me a program in python that asks the user for his: name, year_of_birth, month_of_birth, day_of_birth and then calculates how many days he lived till today and the program welcomes the user and tells him how many days he lived and additionaly his physical wave, emotional wave and intelectual wave.
physical_wave = sin(𝟐𝝅/23ays_old), emotional_wave= sin(2𝝅/28*days_old), intelectual_wave= sin(2𝝅/33*days_old). After calculating the biorhythms, the program should check whether they are high (above0.5) and congratulate on a good result, low (less than -0.5) and console on a bad day. In case of low result, the algorithm also checks whether the next day will bring a higher or lower result. In case of higher score, the program should say something like "Don't worry. Tomorrow will be better!"
"""


def calculate_days_old(birthdate):
    today = datetime.date.today()
    days_old = (today - birthdate).days
    return days_old


def calculate_biorhythms(days_old):
    physical_wave = math.sin(2 * math.pi / 23 * days_old)
    emotional_wave = math.sin(2 * math.pi / 28 * days_old)
    intellectual_wave = math.sin(2 * math.pi / 33 * days_old)
    return physical_wave, emotional_wave, intellectual_wave


def main():
    # Get user input
    name = input("Enter your name: ")
    year_of_birth = int(input("Enter your year of birth: "))
    month_of_birth = int(input("Enter your month of birth: "))
    day_of_birth = int(input("Enter your day of birth: "))

    # Calculate days old and biorhythms
    birthdate = datetime.date(year_of_birth, month_of_birth, day_of_birth)
    days_old = calculate_days_old(birthdate)
    physical_wave, emotional_wave, intellectual_wave = calculate_biorhythms(days_old)

    # Display results
    print(f"Welcome, {name}!")
    print(f"You have lived for {days_old} days.")

    print(f"Your physical wave: {physical_wave}")
    print(f"Your emotional wave: {emotional_wave}")
    print(f"Your intellectual wave: {intellectual_wave}")

    # Check biorhythm conditions
    if physical_wave > 0.5:
        print("Congratulations! Your physical wave is high today.")
    elif physical_wave < -0.5:
        print("Take it easy. Your physical wave is low today.")
        # Check for the next day's prediction
        next_day_physical_wave = math.sin(2 * math.pi / 23 * (days_old + 1))
        if next_day_physical_wave > physical_wave:
            print("Don't worry. Tomorrow will be better!")

    if emotional_wave > 0.5:
        print("Congratulations! Your emotional wave is high today.")
    elif emotional_wave < -0.5:
        print("Take it easy. Your emotional wave is low today.")
        # Check for the next day's prediction
        next_day_emotional_wave = math.sin(2 * math.pi / 28 * (days_old + 1))
        if next_day_emotional_wave > emotional_wave:
            print("Don't worry. Tomorrow will be better!")

    if intellectual_wave > 0.5:
        print("Congratulations! Your intellectual wave is high today.")
    elif intellectual_wave < -0.5:
        print("Take it easy. Your intellectual wave is low today.")
        # Check for the next day's prediction
        next_day_intellectual_wave = math.sin(2 * math.pi / 33 * (days_old + 1))
        if next_day_intellectual_wave > intellectual_wave:
            print("Don't worry. Tomorrow will be better!")


if __name__ == "__main__":
    main()
